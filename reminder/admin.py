from django.contrib import admin
from .models import ClientAppointment, CradenMooreClients, EnishBookings

# Register your models here.

admin.site.register(ClientAppointment)
admin.site.register(CradenMooreClients)
admin.site.register(EnishBookings)
