from django.contrib import admin
from .models import (ClientAppointment, CradenMooreClients, 
                     EnishBookings, LaundryClinicCustomerQuery, 
                     LaundryClinicEnglishSpeakingCustomerQuery,
                     LaundryClinicSpanishSpeakingCustomerQuery,
                     LaundryClinicVoiceCall,
                     CeraCerni)

# Register your models here.

admin.site.register(ClientAppointment)
admin.site.register(CradenMooreClients)
admin.site.register(EnishBookings)
admin.site.register(LaundryClinicCustomerQuery)
admin.site.register(LaundryClinicEnglishSpeakingCustomerQuery)
admin.site.register(LaundryClinicSpanishSpeakingCustomerQuery)
admin.site.register(LaundryClinicVoiceCall)
admin.site.register(CeraCerni)
