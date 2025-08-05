from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from .user import User
from .tour import Tour
from .booking import Booking


class Review(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews'
    )
    tour = models.ForeignKey(
        Tour, on_delete=models.CASCADE, related_name='reviews'
    )
    booking = models.ForeignKey(
        Booking, on_delete=models.CASCADE, related_name='reviews',
        blank=True, null=True
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'reviews'
        indexes = [
            models.Index(fields=['user'], name='idx_review_user_id'),
            models.Index(fields=['tour'], name='idx_review_tour_id'),
            models.Index(fields=['rating'], name='idx_review_rating'),
        ]

    def __str__(self):
        return f"Review by {self.user.full_name} for {self.tour.title}"
