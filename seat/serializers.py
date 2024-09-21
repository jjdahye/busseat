# seat/serializers.py
from rest_framework import serializers
from .models import Seat, Stop, Bus

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id', 'seat_number', 'status', 'bus']
