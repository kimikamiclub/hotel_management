from django.contrib import admin
from app.models import Room, Client, Booking, Hotel

admin.site.register(Room)
admin.site.register(Hotel)
admin.site.register(Booking)
admin.site.register(Client)

