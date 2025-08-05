from django.db import models
from django.utils import timezone
from ..common.constants import BookingStatus
from .user import User
from .tour import Tour
from .tour_trip import TourTrip


class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookings'
    )
    tour = models.ForeignKey(
        Tour, on_delete=models.CASCADE, related_name='bookings'
    )
    trip = models.ForeignKey(
        TourTrip, on_delete=models.CASCADE, related_name='bookings'
    )
    adult_count = models.IntegerField(default=1)
    child_count = models.IntegerField(default=0)
    single_supplement_count = models.IntegerField(default=0)
    double_supplement_count = models.IntegerField(default=0)
    family_supplement_count = models.IntegerField(default=0)
    total_amount = models.DecimalField(
        max_digits=12, decimal_places=2, default=0
    )
    discount_amount = models.DecimalField(
        max_digits=12, decimal_places=2, default=0
    )
    final_amount = models.DecimalField(
        max_digits=12, decimal_places=2, default=0
    )
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    customer_address = models.TextField()
    emergency_contact_name = models.CharField(max_length=255)
    emergency_contact_phone = models.CharField(max_length=20)
    special_requests = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20, choices=BookingStatus.CHOICES,
        default=BookingStatus.PENDING
    )
    cancelled_at = models.DateTimeField(blank=True, null=True)
    cancellation_reason = models.TextField(blank=True, null=True)
    refund_amount = models.DecimalField(
        max_digits=12, decimal_places=2, null=True
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bookings'
        indexes = [
            models.Index(fields=['user'], name='idx_booking_user_id'),
            models.Index(fields=['tour'], name='idx_booking_tour_id'),
            models.Index(fields=['trip'], name='idx_booking_trip_id'),
            models.Index(fields=['status'], name='idx_booking_status'),
        ]

    def __str__(self):
        return f"Booking #{self.id} - {self.customer_name}"
