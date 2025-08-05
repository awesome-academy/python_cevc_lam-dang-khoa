from django.db import models
from django.utils import timezone
from .review import Review


class ReviewImage(models.Model):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='review_images'
    )
    image = models.ImageField(upload_to='reviews/')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'review_images'
        indexes = [
            models.Index(fields=['review'], name='idx_review_image_review_id'),
        ]

    def __str__(self):
        return f"Review {self.review.id} - Image {self.id}"
