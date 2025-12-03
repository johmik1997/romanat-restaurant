from django.urls import path, include
from rest_framework import routers
from .views import (
    ContactMessageCreateView, CustomerCancelReservationView, CustomerReservationView, UserListView, UserViewSet, RoleViewSet, PermissionViewSet, RolePermissionViewSet,
     CustomerSignupView
)
from .custom_jwt_claim import CustomTokenObtainPairView


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'role-permissions', RolePermissionViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path("list/", UserListView.as_view(), name="user-list"),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('signup/', CustomerSignupView.as_view(), name='customer_signup'),
    path("contact/", ContactMessageCreateView.as_view(), name="contact-create"),
    path('customer/reservation/', CustomerReservationView.as_view(), name='customer-reservation'),
    path('customer/reservation/<int:reservation_id>/cancel/', CustomerCancelReservationView.as_view(), name='customer-cancel-reservation'),

]
