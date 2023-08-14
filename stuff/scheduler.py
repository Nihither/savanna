from django.http import HttpResponse
from .models import Student, Teacher
from datetime import datetime, timedelta
import requests


def birthday_notification(request):
    bot_token = '6120853183:AAFAkD0XFkS3p_ZckGOCDadTG6K4eQ8T0tA'
    chat_id = '-1001799471579'
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    date_today = datetime.today()
    text = ''
    for i in (1, 2):
        delta = timedelta(days=i)
        d = date_today + delta
        students = Student.objects.filter(birthday__month=d.month) & Student.objects.filter(birthday__day=d.day)
        if students:
            text = text + f'Дни рождения учеников {d.day} {d.strftime("%b")} \n\n'
            for student in students:
                text = text + f"{student.first_name} {student.last_name}\n" \
                              f"Контакт ученика: {student.contact}\n" \
                              f"Родитель: {student.parent_first_name} {student.parent_last_name}\n" \
                              f"Контакт родителя: {student.parent_contact}\n\n"
        teachers = Teacher.objects.filter(birthday__month=d.month) & Teacher.objects.filter(birthday__day=d.day)
        if teachers:
            text = text + f'Дни рождения сотрудников {d.day} {d.strftime("%b")} \n\n'
            for teacher in teachers:
                text = text + f"{teacher.first_name} {teacher.last_name}\n" \
                              f"Контакт : {teacher.contact}\n\n"

    params = {
        'chat_id': chat_id,
        'text': text
    }
    if text:
        r = requests.post(url=url, params=params)

    return HttpResponse(request, r.status_code)
