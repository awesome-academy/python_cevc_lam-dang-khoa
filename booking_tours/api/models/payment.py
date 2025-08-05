from django.db import models
from django.utils import timezone
from ..common.constants import PaymentMethod, PaymentStatus
from .booking import Booking


class Payment(models.Model):
    booking = models.ForeignKey(
        Booking, on_delete=models.CASCADE, related_name='payments'
    )
    transaction_id = models.CharField(
        max_length=255, unique=True, blank=True, null=True
    )
    payment_method = models.CharField(
        max_length=20, choices=PaymentMethod.CHOICES,
        default=PaymentMethod.CREDIT_CARD
    )
    bank_code = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(
        max_length=20, choices=PaymentStatus.CHOICES,
        default=PaymentStatus.PENDING
    )
    gateway_response = models.JSONField(blank=True, null=True)
    paid_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'payments'
        indexes = [
            models.Index(fields=['booking'], name='idx_payment_booking_id'),
            models.Index(
                fields=['transaction_id'], name='idx_payment_transaction_id'
            ),
            models.Index(fields=['status'], name='idx_payment_status'),
        ]

    def __str__(self):
        return f"Payment #{self.id} - {self.booking.customer_name}"
