from rest_framework import serializers
from .models import ClientAppointment, CradenMooreClients, EnishBookings

class ClientAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientAppointment
        fields = "__all__"


class CradenMooreClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CradenMooreClients
        fields = "__all__"


class EnishBookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnishBookings
        fields = "__all__"