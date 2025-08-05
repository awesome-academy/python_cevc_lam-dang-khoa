from django.db import models
from django.utils import timezone
from ..common.constants import TourGuideStatus


class TourGuide(models.Model):
    full_name = models.TextField()
    phone_number = models.TextField(blank=True, null=True)
    specialties = models.TextField(blank=True, null=True)
    languages = models.TextField(blank=True, null=True)
    experience_years = models.IntegerField(default=0)
    license_number = models.CharField(max_length=100, blank=True, null=True)
    total_trips = models.IntegerField(default=0)
    bio = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=10, choices=TourGuideStatus.CHOICES,
        default=TourGuideStatus.ACTIVE
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tour_guides'

    def __str__(self):
        return self.full_name
