from django.db import models
from django.conf import settings
from reservations.models import Reservation


class Payment(models.Model):
    PAYMENT_METHODS = [
        ("cash", "Cash"),
        ("card", "Card"),
        ("bank", "Bank Transfer"),
        ("mobile", "Mobile Money / Chapa"),
    ]

    PAYMENT_STATUS = [
        ("paid", "Paid"),
        ("pending", "Pending"),
        ("failed", "Failed"),
        ("refunded", "Refunded"),
    ]

    reservation = models.ForeignKey(
        Reservation,
        on_delete=models.CASCADE,
        related_name="payments"
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=20, choices=PAYMENT_METHODS, default="mobile")

    status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default="pending")

    # Chapa fields
    tx_ref = models.CharField(max_length=100, unique=True)  # Your unique reference
    chapa_reference = models.CharField(max_length=100, null=True, blank=True)  # Chapa's ID

    paid_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="payments_processed"
    )

    paid_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-paid_at"]

    def __str__(self):
        return f"Payment {self.tx_ref} - {self.status}"
