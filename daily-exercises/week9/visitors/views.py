import calendar
from datetime import datetime

from django.shortcuts import render

from .calendar import HTMLEventCalendar, Util
from .models import Room


def info_page(request):
    return render(request, 'visitors/info.html')


def index(request):
    return render(request, 'visitors/info.html')


def show_vacancies(request):
    now = datetime.now()
    start_date = Util.get_month_start_date(now)
    end_date = Util.get_month_end_date(now)
    free_rooms = Room.get_free_rooms(start_date, end_date, daily=True)
    for date, rooms_count in free_rooms.items():
        free_rooms[date] = "{} rooms".format(rooms_count)

    cal = HTMLEventCalendar(calendar.SUNDAY, events=free_rooms)
    context = {
        'calendar': cal.formatmonth(now.year, now.month)
    }
    return render(request, 'visitors/vacancies.html', context)
