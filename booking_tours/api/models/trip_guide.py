from django.db import models


class TripGuide(models.Model):
    tour_trip = models.ForeignKey(
        'TourTrip', on_delete=models.CASCADE, related_name='trip_guides'
    )
    tour_guide = models.ForeignKey(
        'TourGuide', on_delete=models.CASCADE, related_name='trip_assignments'
    )

    class Meta:
        db_table = 'trip_guides'
        unique_together = ('tour_trip', 'tour_guide')
        indexes = [
            models.Index(
                fields=['tour_trip'], name='idx_trip_guide_tour_trip'
            ),
            models.Index(
                fields=['tour_guide'], name='idx_trip_guide_tour_guide'
            ),
        ]

    def __str__(self):
        return f"{self.tour_trip} - {self.tour_guide.full_name}"
