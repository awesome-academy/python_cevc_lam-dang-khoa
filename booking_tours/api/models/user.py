from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from ..common.constants import UserGender, UserStatus


class User(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(
        max_length=10, choices=UserGender.CHOICES, blank=True, null=True
    )
    address = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=10, choices=UserStatus.CHOICES, default=UserStatus.INACTIVE
    )
    email_verified = models.BooleanField(default=False)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name']

    class Meta:
        db_table = 'users'
        indexes = [
            models.Index(fields=['email'], name='idx_email'),
            models.Index(fields=['status'], name='idx_status'),
        ]

    def __str__(self):
        return self.full_name or self.email
