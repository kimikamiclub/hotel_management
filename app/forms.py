from django import forms
from django.contrib.auth.models import User

from .models import Room, Booking, Client


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('name', 'description', 'categories', 'capacity', 'image',)


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('user_info', 'name_room', 'date', 'payment')


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'surname', 'phone', 'email')
