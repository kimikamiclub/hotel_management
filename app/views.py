from django.shortcuts import render, redirect
from django.http import HttpResponse

from app.forms import ContactForm, ClientForm, ReservationForm, RoomForm
from app.models import Room, Booking, Client


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def home_page(request):
    return render(request, "templates/home_page.html")


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, "templates/contact.html", {"form": form})


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
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.save()
            return redirect('contact_success')
    else:
        form = ReservationForm()
    return render(request, "templates/room_booking.html", {'form': form})


def create_room(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.save()
            return redirect('contact_success')
    else:
        form = RoomForm
    return render(request, "templates/room_create.html", {'form': form})


def view_clients(request):
    clients = Client.objects.all()
    return render(request, "templates/client_view.html", {"clients": clients})


def create_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            return redirect('contact_success')
    else:
        form = ClientForm()
    return render(request, "templates/client_create.html", {"form": form})


def contact_success(request):
    return render(request, "templates/success_page.html")
