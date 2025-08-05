from django.db import models
from django.utils import timezone
from .tour import Tour


class TourImage(models.Model):
    tour = models.ForeignKey(
        Tour, on_delete=models.CASCADE, related_name='images'
    )
    image = models.ImageField(upload_to='tours/', blank=True, null=True)
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'tour_images'
        indexes = [
            models.Index(fields=['tour'], name='idx_tour_image_tour_id'),
            models.Index(
                fields=['sort_order'], name='idx_tour_image_sort_order'
            ),
        ]

    def __str__(self):
        return f"{self.tour.title} - Image {self.id}"
