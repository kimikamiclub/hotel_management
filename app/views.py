from django.shortcuts import render
from django.http import HttpResponse
from app.models import Room, Booking


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def home_page(request):
    return render(request, "templates/home_page.html")


def contact(request):
    return render(request, "templates/contact.html")


def rooms_list(request):
    rooms = Room.objects.all()
    return render(request, "templates/rooms_list.html", {"rooms": rooms})


def reservations_list(request):
    reservations = Booking.objects.all()
    return render(request, "templates/reservations_list.html", {"reservations": reservations})


def view_reservations(request):
    reservations = Booking.objects.all()
    return render(request, "templates/view_reservations.html", {"reservations": reservations})


def make_reservation(request):
    return render(request, "templates/room_booking.html")
