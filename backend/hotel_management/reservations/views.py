from rest_framework import viewsets, permissions, status, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from django.db.models import Q
from accounts.permissions import RoleBasedPermission
from reservations.models import Reservation
from reservations.serializers import ReservationSerializer
from django.db import transaction


class ReservationViewSet(viewsets.ModelViewSet):
    """
    Manage reservations.
    Customers: can create and view their own reservations.
    Admin/Manager: can view all and manage reservations.
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        'booking_id',
        'customer__first_name',
        'customer__last_name',
        'customer__email',
        'room__room_number',
        'room__room_type__name',
        'special_requests',
    ]
    ordering_fields = [
        'check_in', 
        'check_out', 
        'total_price', 
        'created_at',
        'updated_at',
        'status'
    ]
    ordering = ['-created_at']
    filterset_fields = ['status']

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        
        # Apply user-specific filtering
        if not (user.is_superuser or (hasattr(user, 'role') and user.role and user.role.name in ['Admin', 'Manager', 'Receptionist'])):
            queryset = queryset.filter(customer=user)
        
        # Get filter parameters from request
        check_in_from = self.request.query_params.get('check_in_from')
        check_in_to = self.request.query_params.get('check_in_to')
        check_out_from = self.request.query_params.get('check_out_from')
        check_out_to = self.request.query_params.get('check_out_to')
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        room_type = self.request.query_params.get('room_type')
        room_number = self.request.query_params.get('room_number')
        customer_name = self.request.query_params.get('customer_name')
        
        # Apply date filters
        if check_in_from:
            queryset = queryset.filter(check_in__gte=check_in_from)
        if check_in_to:
            queryset = queryset.filter(check_in__lte=check_in_to)
        if check_out_from:
            queryset = queryset.filter(check_out__gte=check_out_from)
        if check_out_to:
            queryset = queryset.filter(check_out__lte=check_out_to)
        
        # Apply price filters
        if min_price:
            try:
                queryset = queryset.filter(total_price__gte=float(min_price))
            except (ValueError, TypeError):
                pass
        if max_price:
            try:
                queryset = queryset.filter(total_price__lte=float(max_price))
            except (ValueError, TypeError):
                pass
        
        # Apply room filters
        if room_type:
            queryset = queryset.filter(room__room_type__name__icontains=room_type)
        if room_number:
            queryset = queryset.filter(room__room_number__icontains=room_number)
        
        # Apply customer name filter
        if customer_name:
            queryset = queryset.filter(
                Q(customer__first_name__icontains=customer_name) |
                Q(customer__last_name__icontains=customer_name)
            )
        
        return queryset

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'create']:
            return [permissions.IsAuthenticated()]
    
        self.required_permission = 'manage_reservations'
        return [RoleBasedPermission()]

    def perform_create(self, serializer):
        serializer.save(
            customer=self.request.user 
                if not (self.request.user.role and 
                        self.request.user.role.name in ['Admin', 'Manager', 'Receptionist'])
                else serializer.validated_data.get("customer"),
            created_by=self.request.user
        )

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    @action(detail=True, methods=['post'], url_path='cancel')
    def cancel_reservation(self, request, pk=None):
        reservation = self.get_object()
        user = request.user

        # Only owner or staff/admin can cancel
        if reservation.customer != user and not (user.is_superuser or (user.role and user.role.name in ['Admin', 'Manager'])):
            return Response({"detail": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)

        if reservation.status == 'cancelled':
            return Response({"detail": "Reservation is already cancelled"}, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            old_status = reservation.status
            reservation.status = 'cancelled'
            reservation.cancelled_at = timezone.now()
            reservation.save()
            
            # If cancelling a checked-in reservation, free the room
            if old_status == 'checked_in' and reservation.room.status == 'occupied':
                reservation.room.status = 'available'
                reservation.room.save(update_fields=['status'])
        
        return Response({
            "status": "Reservation cancelled",
            "room_status": reservation.room.status
        }, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], url_path='check-in')
    def check_in(self, request, pk=None):
        reservation = self.get_object()
        user = request.user
        
        # Check permissions
        if not (user.is_superuser or (user.role and user.role.name in ['Admin', 'Manager', 'Receptionist'])):
            return Response({"detail": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)

        if reservation.status == 'checked_in':
            return Response({"detail": "Reservation is already checked in"}, status=status.HTTP_400_BAD_REQUEST)

        if reservation.status != 'confirmed':
            return Response({"detail": "Only confirmed reservations can be checked in"}, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            reservation.status = 'checked_in'
            reservation.checked_in_at = timezone.now()
            reservation.save()
            
            # Update room status to occupied
            reservation.room.status = 'occupied'
            reservation.room.save(update_fields=['status'])
        
        return Response({
            "status": "Guest checked in successfully",
            "room_status": reservation.room.status
        }, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], url_path='check-out')
    def check_out(self, request, pk=None):
        reservation = self.get_object()
        user = request.user
        
        # Check permissions
        if not (user.is_superuser or (user.role and user.role.name in ['Admin', 'Manager', 'Receptionist'])):
            return Response({"detail": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)

        if reservation.status == 'checked_out':
            return Response({"detail": "Reservation is already checked out"}, status=status.HTTP_400_BAD_REQUEST)

        if reservation.status != 'checked_in':
            return Response({"detail": "Only checked-in reservations can be checked out"}, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            reservation.status = 'checked_out'
            reservation.checked_out_at = timezone.now()
            reservation.save()
            
            # Update room status to available
            if reservation.room.status == 'occupied':
                reservation.room.status = 'available'
                reservation.room.save(update_fields=['status'])
        
        return Response({
            "status": "Guest checked out successfully",
            "room_status": reservation.room.status
        }, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], url_path='confirm')
    def confirm_reservation(self, request, pk=None):
        reservation = self.get_object()
        user = request.user
        if not (user.is_superuser or (user.role and user.role.name in ['Admin', 'Manager'])):
            return Response({"detail": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)

        if reservation.status == 'confirmed':
            return Response({"detail": "Reservation is already confirmed"}, status=status.HTTP_400_BAD_REQUEST)

        reservation.status = 'confirmed'
        reservation.confirmed_at = timezone.now()
        reservation.save()
        return Response({"status": "Reservation confirmed"}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='stats')
    def get_stats(self, request):
        """Get reservation statistics"""
        user = request.user
        
        # Base queryset based on user role
        if user.is_superuser or (hasattr(user, 'role') and user.role and user.role.name in ['Admin', 'Manager', 'Receptionist']):
            queryset = Reservation.objects.all()
        else:
            queryset = Reservation.objects.filter(customer=user)
        
        # Apply date filters if provided
        check_in_from = request.query_params.get('check_in_from')
        check_in_to = request.query_params.get('check_in_to')
        
        if check_in_from:
            queryset = queryset.filter(check_in__gte=check_in_from)
        if check_in_to:
            queryset = queryset.filter(check_in__lte=check_in_to)
        
        total = queryset.count()
        confirmed = queryset.filter(status='confirmed').count()
        checked_in = queryset.filter(status='checked_in').count()
        checked_out = queryset.filter(status='checked_out').count()
        cancelled = queryset.filter(status='cancelled').count()
        pending = queryset.filter(status='pending').count()
        
        # Calculate revenue
        revenue = queryset.filter(status__in=['confirmed', 'checked_in', 'checked_out']).aggregate(
            total_revenue=models.Sum('total_price')
        )['total_revenue'] or 0
        
        return Response({
            'total': total,
            'confirmed': confirmed,
            'checked_in': checked_in,
            'checked_out': checked_out,
            'cancelled': cancelled,
            'pending': pending,
            'revenue': float(revenue),
        })

    @action(detail=False, methods=['post'], url_path='bulk-update')
    def bulk_update_status(self, request):
        """Bulk update reservation statuses"""
        user = request.user
        
        # Check permissions
        if not (user.is_superuser or (user.role and user.role.name in ['Admin', 'Manager', 'Receptionist'])):
            return Response({"detail": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)
        
        reservation_ids = request.data.get('reservation_ids', [])
        new_status = request.data.get('status')
        
        if not reservation_ids or not new_status:
            return Response(
                {"error": "reservation_ids and status are required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Validate status
        valid_statuses = ['pending', 'confirmed', 'checked_in', 'checked_out', 'cancelled']
        if new_status not in valid_statuses:
            return Response(
                {"error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Get reservations that the user has permission to update
        reservations = Reservation.objects.filter(id__in=reservation_ids)
        
        # Update each reservation with proper room status handling
        updated_count = 0
        with transaction.atomic():
            for reservation in reservations:
                old_status = reservation.status
                reservation.status = new_status
                
                # Set timestamps
                if new_status == 'checked_in':
                    reservation.checked_in_at = timezone.now()
                elif new_status == 'checked_out':
                    reservation.checked_out_at = timezone.now()
                elif new_status == 'cancelled':
                    reservation.cancelled_at = timezone.now()
                
                reservation.save()
                
                # Update room status
                room = reservation.room
                if new_status == 'checked_in' and room.status != 'occupied':
                    room.status = 'occupied'
                    room.save(update_fields=['status'])
                elif new_status == 'checked_out' and room.status == 'occupied':
                    room.status = 'available'
                    room.save(update_fields=['status'])
                elif new_status == 'cancelled' and old_status == 'checked_in' and room.status == 'occupied':
                    room.status = 'available'
                    room.save(update_fields=['status'])
                
                updated_count += 1
        
        return Response({
            "message": f"Successfully updated {updated_count} reservation(s) to {new_status}",
            "updated_count": updated_count
        }, status=status.HTTP_200_OK)


class ReservationStatusUpdateView(APIView):
    def patch(self, request, pk):
        try:
            reservation = Reservation.objects.get(id=pk)
        except Reservation.DoesNotExist:
            return Response({"error": "Reservation not found"}, status=404)

        new_status = request.data.get("status")

        allowed_status = [
            "pending",
            "confirmed",
            "checked_in",
            "checked_out",
            "cancelled"
        ]

        if not new_status:
            return Response({"error": "Status field is required"}, status=400)

        if new_status not in allowed_status:
            return Response({"error": "Invalid status"}, status=400)

        # Get old status for room update logic
        old_status = reservation.status
        
        # Use transaction to ensure both updates succeed or fail together
        with transaction.atomic():
            # Update reservation status
            reservation.status = new_status
            
            # Set timestamps for certain status changes
            if new_status == 'checked_in':
                reservation.checked_in_at = timezone.now()
            elif new_status == 'checked_out':
                reservation.checked_out_at = timezone.now()
            elif new_status == 'cancelled':
                reservation.cancelled_at = timezone.now()
            
            reservation.save()
            
            # Update room status based on reservation status
            room = reservation.room
            
            if new_status == 'checked_in':
                room.status = 'occupied'
                room.save(update_fields=['status'])
            
            elif new_status == 'checked_out':
                if room.status == 'occupied':
                    room.status = 'available'
                    room.save(update_fields=['status'])
            
            elif new_status == 'cancelled':
                # If cancelling a checked-in reservation, free the room
                if old_status == 'checked_in' and room.status == 'occupied':
                    room.status = 'available'
                    room.save(update_fields=['status'])

        return Response({
            "message": "Reservation status updated successfully",
            "reservation_id": reservation.id,
            "status": new_status,
            "room_status": reservation.room.status
        }, status=200)