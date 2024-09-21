# seat/admin.py
from django.contrib import admin
from .models import Stop, Bus, Seat

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('seat_number', 'status')
    list_filter = ('status', )

