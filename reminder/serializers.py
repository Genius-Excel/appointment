from rest_framework import serializers
from .models import ClientAppointment

class ClientAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientAppointment
        fields = "__all__"