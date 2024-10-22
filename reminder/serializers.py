from rest_framework import serializers
from .models import (ClientAppointment, CradenMooreClients, EnishBookings,
                      LaundryClinicCustomerQuery, LaundryClinicEnglishSpeakingCustomerQuery,
                      LaundryClinicSpanishSpeakingCustomerQuery)

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


class LaundryClinicCustomerQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = LaundryClinicCustomerQuery
        fields = "__all__"


class LaundryClinicSpanishSpeakingCustomerQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = LaundryClinicSpanishSpeakingCustomerQuery
        fields = "__all__"


class LaundryClinicEnglishSpeakingCustomerQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = LaundryClinicEnglishSpeakingCustomerQuery
        fields = "__all__"