from rest_framework import viewsets, status,generics,filters
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response

from reservations.models import Reservation
from reservations.serializers import ReservationSerializer
from .models import User, Role, Permission, RolePermission
from .serializers import ContactMessageSerializer, UserSerializer, RoleSerializer, PermissionSerializer, RolePermissionSerializer , CustomerRegistrationSerializer
from .permissions import RoleBasedPermission
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [RoleBasedPermission]
    required_permission = "manage_roles"
    paginator =None




class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [RoleBasedPermission]
    required_permission = "manage_permissions"
    paginator =None




class RolePermissionViewSet(viewsets.ModelViewSet):
    queryset = RolePermission.objects.all()
    serializer_class = RolePermissionSerializer
    permission_classes = [RoleBasedPermission]
    required_permission = "assign_permissions"
    paginator =None

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [RoleBasedPermission]
    required_permission = "manage_users"
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'email', 'role__name']
    ordering_fields = ['id', 'first_name', 'last_name', 'email']

    @action(detail=True, methods=['post'], url_path='change-password')
    def change_password(self, request, pk=None):
        user = self.get_object()
        password = request.data.get('password')

        if not password:
            return Response({"error": "Password required"}, status=400)

        user.set_password(password)
        user.save()

        return Response({"message": "Password updated"})

class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()

        role = self.request.query_params.get("role")

        if role and role.lower() == "customer":
            qs = qs.filter(role__name__iexact="Customer")

        return qs



class CustomerSignupView(generics.CreateAPIView):
    serializer_class = CustomerRegistrationSerializer
    permission_classes = []  # Public endpoint, no auth required

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "Customer account created successfully",
                "username": user.username,
                "id": user.id
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactMessageCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Your message has been received. We'll reply soon."},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CustomerReservationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get the first active reservation for the logged-in user
        reservation = Reservation.objects.filter(
            customer=request.user,
            status__in=['pending', 'confirmed', 'checked_in']
        ).first()

        if reservation:
            serializer = ReservationSerializer(reservation)
            return Response(serializer.data, status=200)

        return Response({"reservation": None}, status=200)

class CustomerCancelReservationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, reservation_id):
        try:
            reservation = Reservation.objects.get(id=reservation_id, customer=request.user)
        except Reservation.DoesNotExist:
            return Response({"error": "Reservation not found or not yours"}, status=status.HTTP_404_NOT_FOUND)

        if reservation.status == "cancelled":
            return Response({"error": "Reservation is already cancelled"}, status=status.HTTP_400_BAD_REQUEST)

        reservation.status = "cancelled"
        reservation.save()

        serializer = ReservationSerializer(reservation)
        return Response({"message": "Reservation cancelled successfully", "reservation": serializer.data})