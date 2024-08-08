from django.shortcuts import render
from rest_framework import generics
from .models import ClientAppointment, CradenMooreClients
from .serializers import ClientAppointmentSerializer, CradenMooreClientsSerializer
from django.http import HttpResponse
from .utils import custom_email_sender, custom_sms_sender

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
       
    



def home(request):
    return HttpResponse("The number has been sumed")

