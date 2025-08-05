from django.db import models
from django.utils import timezone
from ..common.constants import TourTripStatus
from .tour import Tour


class TourTrip(models.Model):
    tour = models.ForeignKey(
        Tour, on_delete=models.CASCADE, related_name='trips'
    )
    status = models.CharField(
        max_length=20, choices=TourTripStatus.CHOICES,
        default=TourTripStatus.BOOKING
    )
    departure_date = models.DateField()
    return_date = models.DateField()
    departure_location = models.CharField(max_length=255)
    adult_price = models.DecimalField(max_digits=12, decimal_places=2)
    child_price = models.DecimalField(max_digits=12, decimal_places=2)
    single_supplement = models.DecimalField(
        max_digits=12, decimal_places=2, default=0
    )
    double_supplement = models.DecimalField(
        max_digits=12, decimal_places=2, default=0
    )
    family_supplement = models.DecimalField(
        max_digits=12, decimal_places=2, default=0
    )
    available_slots = models.IntegerField()
    booked_slots = models.IntegerField(default=0)
    special_notes = models.TextField(blank=True, null=True)
    registration_deadline = models.DateField(blank=True, null=True)
    cancellation_deadline = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tour_trips'
        indexes = [
            models.Index(fields=['tour'], name='idx_tour_trip_tour_id'),
            models.Index(
                fields=['departure_date'], name='idx_tour_trip_departure_date'
            ),
            models.Index(fields=['status'], name='idx_tour_trip_status'),
        ]

    def __str__(self):
        return f"{self.tour.title} - {self.departure_date}"
