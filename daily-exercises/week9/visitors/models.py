from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    number = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return "room #{}".format(self.number)

    @staticmethod
    def get_free_rooms(start_date, end_date):
        '''get all rooms without bookings whose:
               start date is before C,
                   and end date is after C
               OR whose start date is on or after C
                   and start date is before D. '''

        bookings_a = Booking.objects.filter(
            start_date__lt=start_date,
            end_date__gt=start_date)
        bookings_b = Booking.objects.filter(
            start_date__gte=start_date,
            start_date__lte=end_date)
        free_rooms = Room.objects.exclude(booking__in=bookings_a) \
            .exclude(booking__in=bookings_b)
        return free_rooms


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return "{}@{}, {} -> {}".format(
            self.customer.username, self.room.number,
            self.start_date, self.end_date)
