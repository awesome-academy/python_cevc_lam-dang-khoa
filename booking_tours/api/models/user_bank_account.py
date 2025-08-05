from django.db import models
from django.utils import timezone
from .user import User


class UserBankAccount(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bank_accounts'
    )
    bank_name = models.CharField(max_length=255)
    bank_code = models.CharField(max_length=50, blank=True, null=True)
    account_number = models.CharField(max_length=50)
    account_holder_name = models.CharField(max_length=255)
    is_default = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_bank_accounts'
        indexes = [
            models.Index(
                fields=['user'], name='idx_user_bank_account_user_id'
            ),
        ]

    def __str__(self):
        return (
            f"{self.user.full_name} - {self.bank_name} "
            f"({self.account_number})"
        )
