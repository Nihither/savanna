from django.shortcuts import render, HttpResponse, get_object_or_404
from django.template import loader
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from .models import Student, Teacher, Subject, SubjectList
from .utils import Calendar


# Index view
@login_required
def index(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    subjects = Subject.objects.all()
    d = get_date()
    students_coming_birthdays_this_week = Student.objects.filter(birthday__week=d.isocalendar().week)
    teachers_coming_birthdays_this_week = Teacher.objects.filter(birthday__week=d.isocalendar().week)
    students_coming_birthdays_next_week = Student.objects.filter(birthday__week=d.isocalendar().week+1)
    teachers_coming_birthdays_next_week = Teacher.objects.filter(birthday__week=d.isocalendar().week+1)
    context_dict = {
        "students": students,
        "teachers": teachers,
        "subjects": subjects,
        "students_coming_birthdays_this_week": students_coming_birthdays_this_week,
        "students_coming_birthdays_next_week": students_coming_birthdays_next_week,
        "teachers_coming_birthdays_this_week": teachers_coming_birthdays_this_week,
        "teachers_coming_birthdays_next_week": teachers_coming_birthdays_next_week,
    }
    return render(request, 'stuff/index.html', context=context_dict)


# Student details vire
@login_required
def student_details(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    context = {"student": student}
    return render(request, 'stuff/student.html', context=context)


# Teacher details view
@login_required
def teacher_details(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    d = datetime.today()
    cal = Calendar(year=d.year, month=d.month)
    html_cal = cal.formatmonth(withyear=True, teacher_id=teacher_id)
    calendar = mark_safe(html_cal)
    context = {
        "teacher": teacher,
        "calendar": calendar
    }
    return render(request, 'stuff/teacher.html', context=context)


# person details view
@login_required
def person_details_view(request, person, person_id):
    if person == 'student':
        person_data = Student.objects.get(pk=person_id)
        subjects = Subject.objects.filter(student=person_id)
    elif person == 'teacher':
        person_data = Teacher.objects.get(pk=person_id)
        subjects = Subject.objects.filter(teacher=person_id)
    context = {
         "person_type": person,
         "person": person_data,
         "subjects": subjects
    }
    template = loader.get_template('stuff/modal_content.html')
    return HttpResponse(template.render(context, request)) 


def get_date():
    return datetime.today()


def get_future_date(delta):
    return get_date() + timedelta(days=delta)
