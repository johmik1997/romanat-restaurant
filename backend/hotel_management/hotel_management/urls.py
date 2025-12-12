from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse

from hotel_management.utils.populate_initial_data import seed_data


# Import the seeder function


def load_seed(request):
    msg = seed_data()
    return HttpResponse(msg)


urlpatterns = [
    path('admin/', admin.site.urls),

    # API Routes
    path('api/accounts/', include('accounts.urls')),
    path('api/', include('rooms.urls')),
    path('api/', include('reservations.urls')),
    path('api/payments/', include('payments.urls')),

    # Seed endpoint
    path("seed-data/", load_seed),
]
