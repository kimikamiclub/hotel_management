from django.db import models


class Hotel(models.Model):
    address = models.CharField(max_length=100)
    capacity = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)


class Client(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    phone_number = models.TextField(max_length=200)
    email = models.EmailField(null=False)


class Room(models.Model):
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    capacity = models.IntegerField(default=0)
    type = models.CharField(max_length=100)
    price = models.IntegerField(default=0)


class Booking(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    number_of_people = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    date = models.DateTimeField('date published')
