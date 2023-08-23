from datetime import date, datetime
from calendar import HTMLCalendar, month_name, day_abbr
from .models import SubjectClass, AvailableTimestamp


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, day, weekday, events, timestamps, teacher_id):
        d_today = datetime.today()
        events_per_day = events.filter(day=weekday).order_by('start_time')
        timestamps_per_day = timestamps.filter(day=weekday).order_by('start_time')
        if events_per_day:
            date_html_class = 'bg-success'
        elif timestamps_per_day:
            date_html_class = 'bg-info'
        else:
            date_html_class = ''
        if day != 0:
            d = date(self.year, self.month, day)

            if d == d_today.date():
                today_class = 'label label-default'
            else:
                today_class = ''
            return f'<td class="{date_html_class} date_in_calendar" day="{day}" month="{self.month}" year="{self.year}" ' \
                   f'teacher="{teacher_id}">' \
                   f'<span class="{today_class}"><small>{day}</small></span>' \
                   f'</td>'
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, events, timestamps, teacher_id):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, weekday, events, timestamps, teacher_id)
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
        timestamps = AvailableTimestamp.objects.filter(teacher=teacher_id)
        cal = f'<table class="table table-bordered">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events, timestamps, teacher_id)}\n'
        cal += f'</tbody></table>'
        return cal
