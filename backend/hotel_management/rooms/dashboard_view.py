from django.utils import timezone
from django.db.models import Count, Sum, Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.models import User
from reservations.models import Reservation
from reservations.serializers import ReservationSerializer
from rooms.models import Room


class ReceptionistDashboardView(APIView):
    def get(self, request):
        today = timezone.now().date()

        # Expected arrivals today
        today_arrivals = Reservation.objects.filter(
            check_in=today,
            status='confirmed'
        ).count()

        # Expected departures today
        today_departures = Reservation.objects.filter(
            check_out=today,
            status='checked-in'
        ).count()

        # In-house guests
        in_house_guests = Reservation.objects.filter(
            status='checked-in'
        ).count()

        # Revenue for today
        today_revenue = (
            Reservation.objects.filter(
                Q(check_in=today) | Q(check_out=today),
                status__in=['confirmed', 'checked-in', 'completed']
            ).aggregate(total=Sum('total_price'))['total'] or 0
        )

        # Today's reservations
        today_reservations = Reservation.objects.filter(
         Q(check_in=today) | Q(check_out=today)
          ).select_related('customer', 'room')


        # Room stats
        total_rooms = Room.objects.count()
        occupied_rooms = Room.objects.filter(status='occupied').count()
        available_rooms = Room.objects.filter(status='available').count()

        occupancy_rate = (
            f"{round((occupied_rooms / total_rooms) * 100)}%"
            if total_rooms > 0 else "0%"
        )

        room_status_counts = list(
            Room.objects.values('status').annotate(count=Count('status'))
        )

        data = {
            "metrics": {
                "expected_arrivals": today_arrivals,
                "expected_departures": today_departures,
                "in_house_guests": in_house_guests,

                "total_rooms": total_rooms,
                "rooms_occupied": occupied_rooms,
                "rooms_available": available_rooms,
                "occupancy_rate": occupancy_rate,

                "revenue_today": today_revenue,
                "total_guests_today": today_arrivals + in_house_guests,

                "walk_ins": 3,
                "average_stay": 2.3,

                "arrival_trend": "up",
                "arrival_trend_value": "12%",
                "departure_trend": "down",
                "departure_trend_value": "5%",
                "occupancy_trend": "stable",
                "availability_trend": "up",
                "availability_trend_value": "8%",
                "guest_trend": "up",
                "guest_trend_value": "15%",
                "pending_trend": "up",
                "pending_trend_value": "20%",
                "revenue_trend": "up",
                "revenue_trend_value": "18%",
            },

            "today_reservations": ReservationSerializer(today_reservations, many=True).data,

            "room_status": room_status_counts,
        }

        return Response(data, status=status.HTTP_200_OK)
