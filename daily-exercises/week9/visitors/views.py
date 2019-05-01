import calendar
from datetime import datetime, timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .calendar import HTMLEventCalendar, Util
from .forms import BookingForm
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


def get_free_rooms(booking):
    return Room.get_free_rooms(
        booking.start_date,
        booking.end_date)


@login_required
def make_booking(request):
    form = BookingForm(initial={
        'start_date': datetime.now(),
        'end_date': datetime.now() + timedelta(days=3)
        })
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # add customer to booking
            booking = form.save(False)
            booking.customer = request.user
            free_rooms = get_free_rooms(booking)
            if len(free_rooms) > 0:
                booking.room = free_rooms[0]
                booking.save()
                messages.info(request, "Your booking is confirmed.")
                return redirect('visitors:info')
            else:
                messages.warning(request, "We cannot have you. Sorry.")

    context = {
        'form': form
    }
    return render(request, 'visitors/make-booking.html', context)
