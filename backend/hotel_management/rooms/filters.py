# rooms/filters.py
import django_filters
from .models import Room

class RoomFilter(django_filters.FilterSet):
    class Meta:
        model = Room
        fields = {
            'status': ['exact'],
            'category': ['exact'],
            'floor': ['exact'],
        }
