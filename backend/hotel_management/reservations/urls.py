from rest_framework import routers
from django.urls import path, include

from reservations.views import ReservationStatusUpdateView, ReservationViewSet

router = routers.DefaultRouter()
router.register(r'reservations', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('reservations/<int:pk>/update-status/', ReservationStatusUpdateView.as_view()),

]