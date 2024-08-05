from django.shortcuts import render
from rest_framework import generics
from .models import ClientAppointment
from .serializers import ClientAppointmentSerializer
from django.http import HttpResponse

# Create your views here.

class CreateClientAppointment(generics.CreateAPIView):
    queryset = ClientAppointment.objects.all()
    serializer_class = ClientAppointmentSerializer


def home(request):
    return HttpResponse("The number has been sumed")

