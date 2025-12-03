from rest_framework import routers
from django.urls import path, include

from rooms.dashboard_view import ReceptionistDashboardView
from .views import ReviewViewSet, RoomTypeViewSet, RoomViewSet

router = routers.DefaultRouter()
router.register(r'room-types', RoomTypeViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/receptionist/', ReceptionistDashboardView.as_view(), name='receptionist-dashboard'),
]
