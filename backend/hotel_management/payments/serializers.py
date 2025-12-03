from rest_framework import serializers
from payments.models import Payment
from reservations.models import Reservation
from accounts.models import User


class PaymentSerializer(serializers.ModelSerializer):
    reservation = serializers.PrimaryKeyRelatedField(read_only=True)
    reservation_id = serializers.PrimaryKeyRelatedField(
        queryset=Reservation.objects.all(),
        source="reservation",
        write_only=True
    )

    paid_by = serializers.PrimaryKeyRelatedField(read_only=True)
    paid_by_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source="paid_by",
        write_only=True,
        required=False
    )

    class Meta:
        model = Payment
        fields = [
            "id", "reservation", "reservation_id", "amount", "method",
            "status", "tx_ref", "chapa_reference",
            "paid_by", "paid_by_id", "paid_at"
        ]
        read_only_fields = ["status", "tx_ref", "chapa_reference", "paid_at"]
