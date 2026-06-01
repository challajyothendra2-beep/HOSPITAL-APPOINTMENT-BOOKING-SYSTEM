from rest_framework import serializers
from .models import appointmentbooking
class AppointmentbookingSerializers(serializers.ModelSerializer):
    class meta:
        model='appointmentbookimg'
        fields='__all__'
        