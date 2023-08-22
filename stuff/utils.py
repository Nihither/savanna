import datetime
from calendar import HTMLCalendar, month_name, day_abbr
from .models import SubjectClass


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, day, weekday, events):
        events_per_day = events.filter(day=weekday).order_by('start_time')
        d = ''
        for event in events_per_day:
            d += f'<li>{event}</li>'
        if day != 0:
            return f'<td><span class="">{day}</span><ul> {d} </ul></td>'
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, weekday, events)
        return f'<tr>{week}</tr>'

    def formatweekday(self, day):
        """
        Return a weekday name as a table header.
        """
        return f'<th class="text-center">{day_abbr[day]}</th>'

    def formatweekheader(self):
        """
        Return a header for a week as a table row.
        """
        s = ''.join(self.formatweekday(i) for i in self.iterweekdays())
        return f'<tr>{s}</tr></thead><tbody>'

    def formatmonthname(self, theyear, themonth, withyear=True):
        """
        Return a month name as a table row.
        """
        if withyear:
            s = f'{month_name[themonth]} {theyear}'
        else:
            s = f'{month_name[themonth]}'
        return f'<thead><tr><th colspan="7" class="text-center">{s}</th></tr>'

    def formatmonth(self, withyear=True, teacher_id=None):
        events = SubjectClass.objects.filter(subject__teacher=teacher_id)
        cal = f'<table class="table table-bordered">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        cal += f'</tbody></table>'
        return cal
