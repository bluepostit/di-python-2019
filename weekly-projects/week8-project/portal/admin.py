from django.contrib import admin

from .models import Event, Person, PersonStatus

admin.site.register(Event)
admin.site.register(Person)
admin.site.register(PersonStatus)
