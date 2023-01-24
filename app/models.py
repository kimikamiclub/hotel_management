from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=250, null=True)
    address = models.CharField(max_length=100)
    capacity = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"


class Client(models.Model):
    name = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    phone_number = models.TextField(max_length=200)
    email = models.EmailField(null=False)

    def __str__(self):
        return f"{self.name} - {self.surname}"


class Room(models.Model):
    name = models.CharField(max_length=300, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    capacity = models.IntegerField(default=0)
    type = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.hotel.name} - {self.name}"


class Booking(models.Model):
    reservation_num = models.IntegerField(default=0, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    number_of_people = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    check_in = models.DateTimeField(' check in date', null=True)
    check_out = models.DateTimeField(' check out date', null=True)

    def __str__(self):
        return f"{self.reservation_num}"




