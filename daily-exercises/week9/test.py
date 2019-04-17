#!/usr/bin/env python3

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel.settings')

django.setup()

from django.contrib.auth.models import User
from visitors.models import Booking, Room

TEST_ROOMS_COUNT = 5


def create_rooms(delete=False):
    if delete:
        Room.objects.all().delete()

    rooms = []
    for i in range(TEST_ROOMS_COUNT):
        room_number = "10{}".format(str(i + 1))
        rooms.append(Room(number=room_number, price=100.00))
    Room.objects.bulk_create(rooms)


def create_bookings(delete=False):
    if delete:
        Booking.objects.all().delete()

    bookings_data = [
        # Week 1
        {
            "room": "101",
            "start": "2019-05-01",
            "end": "2019-05-03"
        },
        {
            "room": "102",
            "start": "2019-05-01",
            "end": "2019-05-03"
        },
        {
            "room": "103",
            "start": "2019-05-06",
            "end": "2019-05-07"
        },
        {
            "room": "104",
            "start": "2019-05-01",
            "end": "2019-05-07"
        },
        {
            "room": "105",
            "start": "2019-05-01",
            "end": "2019-05-06"
        },
        # Week 2
        {
            "room": "101",
            "start": "2019-05-08",
            "end": "2019-05-11"
        },
        {
            "room": "105",
            "start": "2019-05-12",
            "end": "2019-05-13"
        },
    ]

    customer = User.objects.first()
    bookings = []
    for data in bookings_data:
        room = Room.objects.get(number=data['room'])
        booking = Booking(
            room=room,
            start_date=data['start'],
            end_date=data['end'],
            customer=customer)
        bookings.append(booking)
    Booking.objects.bulk_create(bookings)


def show_rooms_and_bookings():
    # print all rooms
    print("~~~ All rooms: ~~~")
    for room in Room.objects.all():
        print(room)

    print("~~~ All bookings: ~~~")
    for booking in Booking.objects.all():
        print(booking)


def show_free_weeks():
    print("~~~ Free weeks: ~~~")
    week_num = 0
    for i in range(1, 22, 7):
        week_num += 1
        start_date = "2019-05-{}".format(i)
        end_date = "2019-05-{}".format(i+7)
        free_rooms = Room.get_free_rooms(start_date, end_date)

        print("Week #{}: {} free rooms:".format(week_num, free_rooms.count()))
        print(free_rooms)


def show_free_days():
    vacancies = {}
    for i in range(10):
        start_date = "2019-05-{}".format(i + 1)
        end_date = "2019-05-{}".format(i + 1)
        free_rooms = Room.get_free_rooms(start_date, end_date)
        vacancies[start_date] = free_rooms

    print("~~~ Vacancies ~~~")
    for day, rooms in vacancies.items():
        print("{}: {} rooms free".format(day, rooms.count()))


def setup():
    create_rooms(True)
    create_bookings(True)


# setup()
show_rooms_and_bookings()
# show_free_weeks()
show_free_days()
