from django.db import models
from django.utils import timezone
from ..common.constants import TourFeatured
from .category import Category


class Tour(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='tours'
    )
    title = models.CharField(max_length=500)
    description = models.TextField()
    destination = models.CharField(max_length=255)
    duration_days = models.IntegerField()
    duration_nights = models.IntegerField()
    base_price = models.DecimalField(max_digits=12, decimal_places=2)
    max_participants = models.PositiveIntegerField()
    min_participants = models.PositiveIntegerField(default=1)
    included_services = models.TextField(blank=True, null=True)
    itinerary = models.TextField(blank=True, null=True)
    terms_conditions = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=True)
    featured = models.CharField(
        max_length=20, choices=TourFeatured.CHOICES,
        default=TourFeatured.NORMAL
    )
    average_rating = models.DecimalField(
        max_digits=3, decimal_places=2, default=0
    )
    total_reviews = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tours'
        indexes = [
            models.Index(fields=['category'], name='idx_tour_category_id'),
            models.Index(fields=['is_public'], name='idx_tour_is_public'),
            models.Index(fields=['featured'], name='idx_tour_featured'),
            models.Index(fields=['base_price'], name='idx_tour_base_price'),
            models.Index(
                fields=['average_rating'], name='idx_tour_average_rating'
            ),
        ]

    def __str__(self):
        return self.title
