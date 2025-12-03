from rest_framework import serializers
from accounts.serializers import UserSerializer
from reservations.models import Reservation
from rooms.serializers import RoomSerializer 


class ReservationSerializer(serializers.ModelSerializer):
    customer = UserSerializer(read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=UserSerializer.Meta.model.objects.all(),
        source='customer',
        write_only=True
    )
    room = RoomSerializer(read_only=True)
    room_id = serializers.PrimaryKeyRelatedField(
        queryset=RoomSerializer.Meta.model.objects.all(),
        source='room',
        write_only=True
    )
    class Meta:
        model = Reservation
        fields = [
            'id', 'customer', 'customer_id', 'room', 'room_id',
            'check_in', 'check_out', 'number_of_guests', 'total_price', 'status','created_at'
        ]
    def validate(self, attrs):
        check_in = attrs['check_in']
        check_out = attrs['check_out']
        room = attrs['room']
        guests = attrs['number_of_guests']

        # Check room availability
        if Reservation.objects.filter(
            room=room,
            check_in__lt=check_out,
            check_out__gt=check_in,
            status__in=['Confirmed', 'Pending']
        ).exists():
            raise serializers.ValidationError("Room not available for selected dates.")

        # Check guest limit
        # if guests > room.capacity:
        #     raise serializers.ValidationError("Number of guests exceeds room capacity.")

        return attrs

