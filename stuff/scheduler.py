from .models import Student
from datetime import datetime, timedelta
import requests


def birthday_notification(request):
    bot_token = '6120853183:AAFAkD0XFkS3p_ZckGOCDadTG6K4eQ8T0tA'
    chat_id = '-1001799471579'
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    d = datetime.today()
    delta = timedelta(days=1)
    d = d + delta
    students = Student.objects.filter(birthday__month=d.month) & Student.objects.filter(birthday__day=d.day)
    text = f'Дни рождения завтра {d.day} {d.strftime("%b")} \n\n'
    for student in students:
        text = text + f"Ученик: {student.first_name} {student.last_name}\n" \
                      f"Контакт ученика: {student.contact}\n" \
                      f"Родитель: {student.parent_first_name} {student.parent_last_name}\n" \
                      f"Контакт родителя: {student.parent_contact}\n\n"
    params = {
        'chat_id': chat_id,
        'text': text
    }

    if students:
        r = requests.post(url=url, params=params)

    return None
