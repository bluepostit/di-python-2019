import calendar
from datetime import datetime


class Util:
    DATE_FORMAT = '%Y-%m-%d'

    def get_month_start_date(datetime):
        return datetime.date().replace(day=1)

    def get_month_end_date(datetime):
        year = datetime.year
        month = datetime.month
        monthrange = calendar.monthrange(year, month)
        return datetime.date().replace(day=monthrange[1])


class CalendarEvent:

    def __init__(self, date, event):
        self.date = date
        self.event = event


class HTMLEventCalendar(calendar.HTMLCalendar):
    # CSS classes for the day <td>s
    cssclasses = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

    # CSS classes for the day <th>s
    cssclasses_weekday_head = cssclasses

    # CSS class for the days before and after current month
    cssclass_noday = "noday"

    # CSS class for the month's head
    cssclass_month_head = "month"

    # CSS class for the month
    cssclass_month = "month"

    # CSS class for the year's table head
    cssclass_year_head = "year"

    # CSS class for the whole year table
    cssclass_year = "year"

    cssclass_event = "calendar-event"

    cssclass_day_number = "day-number"

    def __init__(self, firstweekday=calendar.MONDAY, events={}):
        super().__init__(firstweekday)
        self.events = events

    def get_event(self, day, month, year):
        date = datetime.strptime("{}-{}-{}".format(year, month, day),
                                 Util.DATE_FORMAT)
        date_string = date.strftime(Util.DATE_FORMAT)
        return self.events.get(date_string, '')

    def formatday(self, day, weekday, themonth=None, theyear=None):
        """
        Return a day as a table cell.
        """
        if day == 0:
            # day outside month
            return '<td class="%s">&nbsp;</td>' % self.cssclass_noday
        else:
            event = self.get_event(day, themonth, theyear)
            html = """
            <td class="%s">
              <div class="%s">%s</div>
              <div class="%s">%d</div>
            </td>""" % (self.cssclasses[weekday],
                        self.cssclass_event, event,
                        self.cssclass_day_number, day)
            return html

    def formatweek(self, theweek, themonth=None, theyear=None):
        """
        Return a complete week as a table row.
        """
        s = ''.join(self.formatday(d, wd, themonth, theyear)
                    for (d, wd) in theweek)
        return '<tr>%s</tr>' % s

    def formatmonth(self, theyear, themonth, withyear=True):
        """
        Return a formatted month as a table.
        """
        v = []
        a = v.append
        a('<table border="0" cellpadding="0" cellspacing="0" class="%s">' % (
            self.cssclass_month))
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week, theyear=theyear, themonth=themonth))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)
