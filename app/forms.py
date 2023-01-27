from django import forms
from django.contrib.auth.models import User

from .models import Room, Booking, Client, Contact


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('name', 'hotel', 'capacity', 'price')


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('client', 'room', 'check_in', 'check_out', 'number_of_people')


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'surname', 'phone_number', 'email')


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
