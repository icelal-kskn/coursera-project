from django import forms
from .models import Booking

class BookingForm:
    class Meta:
        model=Booking
        fields='__all__'