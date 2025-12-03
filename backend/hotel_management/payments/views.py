from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
import uuid

from payments.models import Payment
from payments.serializers import PaymentSerializer
from reservations.models import Reservation
from .chapa_service import chapa_initialize_payment, chapa_verify_payment


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role and user.role.name == "superadmin":
            return Payment.objects.all()
        return Payment.objects.filter(paid_by=user)

    # -------------------------
    # Initialize Chapa Payment
    # -------------------------
    @action(detail=False, methods=["post"])
    def initialize(self, request):
        reservation_id = request.data.get("reservation_id")

        try:
            reservation = Reservation.objects.get(id=reservation_id)
        except Reservation.DoesNotExist:
            return Response({"error": "Reservation not found"}, status=404)

        # Customers cannot pay for others
        if request.user != reservation.customer:
            return Response({"error": "Not allowed"}, status=403)

        # Generate unique tx_ref
        tx_ref = f"RES-{reservation.id}-{uuid.uuid4().hex[:8]}"

        # Create payment record
        payment = Payment.objects.create(
            reservation=reservation,
            amount=reservation.total_price,
            method="mobile",
            status="pending",
            tx_ref=tx_ref,
            paid_by=request.user
        )

        # Call Chapa API
        chapa_response = chapa_initialize_payment(
            amount=reservation.total_price,
            email=reservation.customer.email,
            first_name=reservation.customer.first_name,
            last_name=reservation.customer.last_name,
            phone=reservation.customer.phone or "0910000000",
            tx_ref=tx_ref,
            return_url="http://localhost:5173/payment/success",
            callback_url="http://127.0.0.1:8000/api/payments/callback/"
        )

        if chapa_response.get("status") != "success":
            return Response({"error": "Failed to initialize payment", "details": chapa_response}, status=400)

        return Response({
            "checkout_url": chapa_response["data"]["checkout_url"],
            "tx_ref": tx_ref,
            "payment_id": payment.id
        })

    # -------------------------
    # Callback from Chapa
    # -------------------------
    @action(detail=False, methods=["post"])
    def callback(self, request):
        tx_ref = request.data.get("tx_ref")
        status_from_chapa = request.data.get("status")
        chapa_reference = request.data.get("chapa_reference")

        try:
            payment = Payment.objects.get(tx_ref=tx_ref)
        except Payment.DoesNotExist:
            return Response({"error": "Payment not found"}, status=404)

        # Map Chapa status to your model
        if status_from_chapa.lower() == "success":
            payment.status = "paid"
        else:
            payment.status = "failed"

        payment.chapa_reference = chapa_reference
        payment.save()

        # Update reservation if paid
        if payment.status == "paid":
            reservation = payment.reservation
            reservation.status = "Paid"
            reservation.save()

        return Response({"message": "Callback processed"})

    # -------------------------
    # Verify Payment
    # -------------------------
    @action(detail=False, methods=["post"])
    def verify(self, request):
        tx_ref = request.data.get("tx_ref")

        chapa_response = chapa_verify_payment(tx_ref)

        data = chapa_response.get("data")
        if not data:
            return Response({"error": "Chapa verification response missing data", "details": chapa_response}, status=400)

        payment_status = data.get("status")
        chapa_reference = data.get("reference")  # <-- use this instead of "id"
        receipt_url = f"https://chapa.link/payment-receipt/{chapa_reference}" if chapa_reference else None

        # Update local payment record
        try:
            payment = Payment.objects.get(tx_ref=tx_ref)
        except Payment.DoesNotExist:
            return Response({"error": "Payment not found"}, status=404)

        payment.status = payment_status.lower()  # e.g., "failed/cancelled", "paid"
        payment.chapa_reference = chapa_reference
        payment.save()

        # Update reservation only if payment succeeded
        if payment_status.lower() == "paid":
            reservation = payment.reservation
            reservation.status = "Paid"
            reservation.save()

        return Response({
            "message": "Payment verification processed",
            "receipt_url": receipt_url,
            "payment": PaymentSerializer(payment).data,
            "chapa_status": payment_status
        })
