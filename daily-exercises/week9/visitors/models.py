from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth.models import User

from .calendar import Util


def ensure_is_datetime(date):
    if isinstance(date, str):
        date = datetime.strptime(date, Util.DATE_FORMAT)
    return date


class Room(models.Model):
    number = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return "room #{}".format(self.number)

    @staticmethod
    def get_free_rooms(start_date, end_date, **kwargs):
        '''get all rooms without bookings whose:
               start date is before C,
                   and end date is after C
               OR whose start date is on or after C
                   and start date is before D. '''

        if 'daily' in kwargs and (kwargs['daily']):
            return Room.get_daily_free_rooms(start_date, end_date)

        start_date = ensure_is_datetime(start_date)
        end_date = ensure_is_datetime(end_date)

        bookings_a = Booking.objects.filter(
            start_date__lt=start_date,
            end_date__gt=start_date)
        bookings_b = Booking.objects.filter(
            start_date__gte=start_date,
            start_date__lte=end_date)
        free_rooms = Room.objects.exclude(booking__in=bookings_a) \
            .exclude(booking__in=bookings_b)
        return free_rooms

    def get_daily_free_rooms(start_date, end_date):
        '''Get a dictionary mapping date strings to the amount of free
        rooms available on that day.'''

        start_date = ensure_is_datetime(start_date)
        end_date = ensure_is_datetime(end_date)

        if end_date < start_date:
            raise Exception("start date must precede end date")
        frees = {}
        d = start_date
        while d <= end_date:
            rooms = Room.get_free_rooms(d, d)
            d_string = d.strftime(Util.DATE_FORMAT)
            frees[d_string] = rooms.count()
            d = d + timedelta(days=1)

        return frees


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return "{}@{}, {} -> {}".format(
            self.customer.username, self.room.number,
            self.start_date, self.end_date)
