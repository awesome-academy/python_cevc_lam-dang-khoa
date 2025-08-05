from django.db import models
from django.utils import timezone
from .user import User
from .review import Review


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments'
    )
    parent_comment = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True,
        related_name='replies'
    )
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'
        indexes = [
            models.Index(fields=['user'], name='idx_comment_user_id'),
            models.Index(fields=['review'], name='idx_comment_review_id'),
            models.Index(
                fields=['parent_comment'], name='idx_comment_parent_comment_id'
            ),
        ]

    def __str__(self):
        return f"Comment by {self.user.full_name} on review #{self.review.id}"
