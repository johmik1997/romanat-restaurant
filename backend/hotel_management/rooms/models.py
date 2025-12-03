from django.db import models

class RoomType(models.Model):
    """
    Only Single / Double — simple and clean
    """
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    ROOM_STATUS_CHOICES = [
        ("available", "Available"),
        ("occupied", "Occupied"),
        ("maintenance", "Maintenance"),
        ("cleaning", "Cleaning"),
    ]

    room_number = models.CharField(max_length=20, unique=True)
    floor = models.PositiveIntegerField(default=1)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name="rooms")

    title = models.CharField(max_length=150, null=True, blank=True)
    subtitle = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Images
    thumbnail = models.URLField(null=True, blank=True)
    images = models.JSONField(default=list)  # must contain at least 3 image URLs

    category = models.CharField(max_length=50, default="single")  
    size = models.CharField(max_length=50, blank=True)
    view = models.CharField(max_length=100, blank=True)
    capacity = models.CharField(max_length=50, blank=True)

    featured = models.BooleanField(default=False)

    status = models.CharField(max_length=20, choices=ROOM_STATUS_CHOICES, default="available")

    notes = models.TextField(blank=True)
    
    amenities = models.JSONField(default=list)  # ["wifi", "balcony", "air conditioning"]
    about = models.TextField(blank=True)        # longer detailed information

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["floor", "room_number"]

    def __str__(self):
        return f"Room {self.room_number} ({self.room_type.name})"


class Review(models.Model):
    """
    Review model connected to a Room
    """
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="reviews")

    reviewer_name = models.CharField(max_length=100)
    rating = models.PositiveSmallIntegerField(default=5)  # 1–5 stars
    comment = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.room.room_number} - {self.rating}⭐"
