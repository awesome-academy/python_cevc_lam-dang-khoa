from django.db import models
from django.utils import timezone
from .user import User
from .review import Review


class ReviewLike(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='review_likes'
    )
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='likes'
    )
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'review_likes'
        unique_together = [['user', 'review']]
        indexes = [
            models.Index(fields=['review'], name='idx_review_like_review_id'),
        ]

    def __str__(self):
        return f"{self.user.full_name} likes review #{self.review.id}"
