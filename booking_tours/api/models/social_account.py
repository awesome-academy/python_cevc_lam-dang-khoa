from django.db import models
from django.utils import timezone
from ..common.constants import SocialProvider
from .user import User


class SocialAccount(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='social_accounts'
    )
    provider = models.CharField(max_length=20, choices=SocialProvider.CHOICES)
    provider_id = models.CharField(max_length=255)
    provider_email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'social_accounts'
        unique_together = [['provider', 'provider_id']]
        indexes = [
            models.Index(fields=['user'], name='idx_social_account_user_id'),
        ]

    def __str__(self):
        return f"{self.user.full_name} - {self.provider}"
