#!/usr/bin/env python3

import os
import json
import django
import pytest

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel.settings')

django.setup()

from django.contrib.auth.models import User
from visitors.models import Booking, Room

JSON_DATA_FILE = 'test-data.json'


@pytest.fixture(scope="module")
def test_data():
    with open(JSON_DATA_FILE) as f:
        data = json.load(f)
        yield data

    # Cleanup:
    print("cleaning up...")
    # Delete all test rooms
    for room_data in data['rooms']:
        room = Room.objects.get(number=room_data['number'])
        room.delete()
    for cust in data['customers']:
        try:
            customer = User.objects.get(username=cust['username'])
            # Delete all bookings related to the customer
            Booking.objects.filter(customer=customer).delete()
            customer.delete()
        except:
            print("customer not found.")


def create_customers(data, delete=False):
    if delete:
        User.objects.all().delete()

    for cust in data['customers']:
        username = cust['username']
        email = cust['email']
        password = cust['password']
        User.objects.create_user(username, email, password)


def create_rooms(data, delete=False):
    if delete:
        Room.objects.all().delete()

    rooms = []
    for room in data['rooms']:
        room_number = room['number']
        price = float(room['price'])
        rooms.append(Room(number=room_number, price=price))
    Room.objects.bulk_create(rooms)


def create_bookings(data, delete=False):
    if delete:
        Booking.objects.all().delete()

    bookings = []
    for booking_data in data['bookings']:
        room = Room.objects.get(number=booking_data['room'])
        customer = User.objects.get(username=booking_data['username'])
        booking = Booking(
            room=room,
            start_date=booking_data['start'],
            end_date=booking_data['end'],
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


def setup_objects(data):
    create_rooms(data)
    create_customers(data)
    create_bookings(data)


def test_get_free_rooms(test_data):
    setup_objects(test_data)

    free_room_data = test_data['free rooms']
    for item in free_room_data:
        print(item)
        free_rooms = Room.get_free_rooms(item['start'], item['end'])
        assert free_rooms.count() == item['free rooms']
