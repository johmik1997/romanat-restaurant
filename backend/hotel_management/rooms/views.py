from rest_framework import viewsets, permissions, status, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

from .models import Review, RoomType, Room
from .serializers import ReviewSerializer, RoomTypeSerializer, RoomSerializer
from accounts.permissions import RoleBasedPermission

from .filters import RoomFilter   # <-- IMPORTANT


class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]
        self.required_permission = "manage_rooms"
        return [RoleBasedPermission()]


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    # SEARCH + ORDERING + FILTERS
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]

    search_fields = [
        "room_number",
        "room_type__name",
        "category",
        "view",
        "description",
        "floor",
    ]

    ordering_fields = [
        "room_number",
        "price",
        "floor",
        "capacity",
        "created_at",
        "status",
    ]

    ordering = ["room_number"]

    # USE CUSTOM FILTER TO AVOID _set_choices ERROR
    filterset_class = RoomFilter

    def get_queryset(self):
        queryset = Room.objects.all()

        room_type = self.request.query_params.get("room_type__name")
        min_price = self.request.query_params.get("min_price")
        max_price = self.request.query_params.get("max_price")
        price__gte = self.request.query_params.get("price__gte")
        price__lte = self.request.query_params.get("price__lte")

        # Filter by Room Type
        if room_type and room_type != "all":
            queryset = queryset.filter(room_type__name=room_type)

        # Price filtering
        if min_price:
            queryset = queryset.filter(price__gte=float(min_price))
        if max_price:
            queryset = queryset.filter(price__lte=float(max_price))
        if price__gte:
            queryset = queryset.filter(price__gte=float(price__gte))
        if price__lte:
            queryset = queryset.filter(price__lte=float(price__lte))

        return queryset

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]

        self.required_permission = "manage_rooms"
        return [RoleBasedPermission()]

    @action(detail=True, methods=["post"], url_path="mark-unavailable")
    def mark_unavailable(self, request, pk=None):
        self.required_permission = "manage_rooms"

        for perm in self.get_permissions():
            perm.has_permission(request, self)

        room = self.get_object()
        room.status = "maintenance"
        room.save()

        return Response(
            {"status": f"Room {room.room_number} marked unavailable"},
            status=status.HTTP_200_OK,
        )

    @action(detail=True, methods=["get"], url_path="reviews")
    def get_reviews(self, request, pk=None):
        room = self.get_object()
        serializer = ReviewSerializer(room.reviews.all(), many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["post"], url_path="add-review")
    def add_review(self, request, pk=None):
        room = self.get_object()

        data = request.data.copy()
        data["room"] = room.id

        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]

        self.required_permission = "manage_rooms"
        return [RoleBasedPermission()]
