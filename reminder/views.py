from django.shortcuts import render
from datetime import datetime
from rest_framework import generics
from .models import ClientAppointment, CradenMooreClients, EnishBookings
from .serializers import ClientAppointmentSerializer, CradenMooreClientsSerializer, EnishBookingsSerializer
from django.http import HttpResponse
from .utils import custom_email_sender, custom_sms_sender
from django.conf import settings

# Create your views here.

class CreateClientAppointment(generics.CreateAPIView):
    queryset = ClientAppointment.objects.all()
    serializer_class = ClientAppointmentSerializer


class CreateCradenMooreClient(generics.CreateAPIView):
    queryset = CradenMooreClients.objects.all()
    serializer_class = CradenMooreClientsSerializer

    def perform_create(self, serializer):
        user = serializer.save()

        SMS_sender = "Craden Moore Solicitors"
        SMS_meesage = f"Hello {user.first_name}, we recently spoke few minutes ago. Kindly book an appointment with this link:{user.meeting_link}."
        SMS_recipient = user.mobile_number

        custom_sms_sender(SMS_sender, SMS_recipient, SMS_meesage)


class CreateEnishBooking(generics.CreateAPIView):
    queryset = EnishBookings.objects.all()
    serializer_class = EnishBookingsSerializer

    def perform_create(self, serializer):
        user = serializer.save()

        SMS_sender = "Enish"
        SMS_message = f"Hello {user.first_name},\n\n" \
                      f"Your table reservation at {user.restaurant_location} for {user.number_of_guests} guests is confirmed for {user.appointment_date}\n" \
                      f"We look forward to welcoming you!."
        
        SMS_recipient = user.mobile_number
        custom_sms_sender(SMS_sender, SMS_recipient, SMS_message)
        # custom_email_sender(settings.TEST_EMAIL, "Enish Testing", SMS_message, "Enish Restaurant")


       
    



def home(request):
    return HttpResponse("The number has been sumed")


