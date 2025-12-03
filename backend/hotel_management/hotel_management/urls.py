
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')), 
    path('api/', include('rooms.urls')), 
    path('api/', include('reservations.urls')),
    path('api/payments/', include('payments.urls')),

]
