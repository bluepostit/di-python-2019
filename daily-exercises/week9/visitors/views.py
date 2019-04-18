import calendar
from datetime import datetime

from django.shortcuts import render

from .calendar import CalendarEvent, HTMLEventCalendar, Util
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
    print(free_rooms)
    cal = calendar.HTMLCalendar(calendar.SUNDAY)
    context = {
        'calendar': str(cal.formatmonth(now.year, now.month))
    }
    print(context)
    return render(request, 'visitors/vacancies.html', context)
