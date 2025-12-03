# reservations/models.py
from django.db import models
from django.conf import settings
from rooms.models import Room

class Reservation(models.Model):
    RESERVATION_STATUS = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("checked_in", "Checked In"),
        ("checked_out", "Checked Out"),
        ("cancelled", "Cancelled"),
    ]

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reservations"
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name="reservations"
    )
    check_in = models.DateField()
    check_out = models.DateField()
    number_of_guests = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=20, choices=RESERVATION_STATUS, default="pending")
    
    # Timestamps for status changes
    confirmed_at = models.DateTimeField(null=True, blank=True)
    checked_in_at = models.DateTimeField(null=True, blank=True)
    checked_out_at = models.DateTimeField(null=True, blank=True)
    cancelled_at = models.DateTimeField(null=True, blank=True)
    # Audit fields
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_reservations"
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="updated_reservations"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["check_in"]
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"

    def __str__(self):
        return f"Reservation #{self.id} - {self.customer.username}"

    # Calculate total price automatically
    def save(self, *args, **kwargs):
        if self.room and not self.total_price:
            nights = (self.check_out - self.check_in).days
            self.total_price = nights * self.room.price
        
        # Get the old status if updating
        old_status = None
        if self.pk:
            old_status = Reservation.objects.get(pk=self.pk).status
        
        # Save the reservation first
        super().save(*args, **kwargs)
        
        # Update room status based on reservation status
        self.update_room_status(old_status)
    
    def update_room_status(self, old_status=None):
        """Update room status based on reservation status"""
        if not self.room:
            return
        
        if self.status == 'checked_in':
            self.room.status = 'occupied'
            self.room.save(update_fields=['status'])
        
        elif self.status == 'checked_out':
            # Only change to available if the room was occupied by this reservation
            if self.room.status == 'occupied':
                self.room.status = 'available'
                self.room.save(update_fields=['status'])
        
        elif self.status == 'cancelled':
            # If reservation is cancelled and room was occupied, make it available
            if self.room.status == 'occupied' and old_status == 'checked_in':
                self.room.status = 'available'
                self.room.save(update_fields=['status'])