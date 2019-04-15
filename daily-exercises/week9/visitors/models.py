from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    number = models.CharField(max_length=50)
    price = models.FloatField()


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
