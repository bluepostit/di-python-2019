#!/usr/bin/env python3

import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dr.settings')

import django
django.setup()

from faker import Faker

from portal.models import Event, Person, PersonStatus


Event.objects.all().delete()
Person.objects.all().delete()
PersonStatus.objects.all().delete()

fire_event = Event(name='fire_sale')
fire_event.save()

missing_status = PersonStatus(name='missing')
missing_status.save()

safe_status = PersonStatus(name='safe')
safe_status.save()

f = Faker()

for i in range(30):
    first_name = f.first_name()
    last_name = f.last_name()
    id_number = f.itin()
    mobile = f.phone_number()
    email = f.email()
    description = f.sentence()
    event = fire_event
    status = random.choice([safe_status, missing_status])
    person = Person(
        first_name=first_name,
        last_name=last_name,
        id_number=id_number,
        mobile=mobile,
        email=email,
        description=description,
        event=event,
        status=status)
    person.save()
