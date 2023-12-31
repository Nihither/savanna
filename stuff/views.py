from django.shortcuts import render, HttpResponse, get_object_or_404
from django.template import loader
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta, date, time
from .models import Student, Teacher, Subject, SubjectClass, AvailableTimestamp, ExtraClass
from .utils import Calendar
from .forms import AddTeacherForm, AddStudentForm, AssignStudentToTeacherForm, RejectStudentToTeacherForm


# Index view
@login_required
def index(request):
    d = get_date()
    students_coming_birthdays_this_week = Student.objects.filter(birthday__week=d.isocalendar().week)
    teachers_coming_birthdays_this_week = Teacher.objects.filter(birthday__week=d.isocalendar().week)
    students_coming_birthdays_next_week = Student.objects.filter(birthday__week=d.isocalendar().week + 1)
    teachers_coming_birthdays_next_week = Teacher.objects.filter(birthday__week=d.isocalendar().week + 1)
    context_dict = {
        "students_coming_birthdays_this_week": students_coming_birthdays_this_week,
        "students_coming_birthdays_next_week": students_coming_birthdays_next_week,
        "teachers_coming_birthdays_this_week": teachers_coming_birthdays_this_week,
        "teachers_coming_birthdays_next_week": teachers_coming_birthdays_next_week,
    }
    return render(request, 'stuff/index.html', context=context_dict)


# Teacher section
@login_required
def get_teacher_list(request):
    teachers = Teacher.objects.filter(rmv=False)
    context = {
        "teachers": teachers,
    }
    template = loader.get_template('stuff/teacher_list.html')
    return HttpResponse(template.render(context, request))


@login_required
def get_teacher_archive_list(request):
    teachers = Teacher.objects.filter(rmv=True)
    context = {
        "teachers": teachers,
    }
    template = loader.get_template('stuff/teacher_list.html')
    return HttpResponse(template.render(context, request))


@login_required
def get_filtered_teacher_list(request):
    req = request.GET['req']
    print(req)
    teachers = Teacher.objects.filter(first_name__icontains=req, rmv=False) | \
        Teacher.objects.filter(last_name__icontains=req, rmv=False)
    context = {
        "teachers": teachers,
    }
    template = loader.get_template('stuff/teacher_list.html')
    return HttpResponse(template.render(context, request))


@login_required
def subjects_per_teacher(request, teacher_id):
    subjects = Subject.objects.filter(teacher__pk=teacher_id)
    context = {
        "subjects": subjects,
    }
    template = loader.get_template('stuff/subjects_per_teacher.html')
    return HttpResponse(template.render(context, request))


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


@login_required
def add_teacher(request):
    if request.method == 'POST':
        form_data = AddTeacherForm(data=request.POST)
        if form_data.is_valid():
            new_teacher = form_data.save()
            return HttpResponse('Сохранено успешно', status='201')
        else:
            context = {
                "form": form_data,
            }
            template = loader.get_template('stuff/add_teacher.html')
            return HttpResponse(template.render(context, request), status='422')
    else:
        form = AddTeacherForm()
        context = {
            "form": form,
        }
        template = loader.get_template('stuff/add_teacher.html')
        return HttpResponse(template.render(context, request))


@login_required
def delete_teacher(request, teacher_id):
    if request.method == 'POST':
        teacher = get_object_or_404(Teacher, pk=teacher_id)
        teacher.delete()
        return HttpResponse('Запись удалена')


@login_required
def archive_teacher(request, teacher_id):
    if request.method == 'POST':
        teacher = get_object_or_404(Teacher, pk=teacher_id)
        if teacher.rmv:
            teacher.rmv = False
            teacher.save()
            return HttpResponse('Перенесено из Архива')
        else:
            teacher.rmv = True
            teacher.save()
            return HttpResponse('Занесено в Архив')


@login_required
def assign_stud_to_teach(request, teacher_id):
    if request.method == 'POST':
        teacher = Teacher.objects.get(pk=teacher_id)
        form_data = AssignStudentToTeacherForm(data=request.POST)
        if form_data.is_valid():
            new_subject = form_data.save(commit=False)
            new_subject.teacher = teacher
            new_subject.save()
            return HttpResponse('Добавлено успешно', status='201')
        else:
            context = {
                "form": form_data,
            }
            template = loader.get_template('stuff/assign_student_to_teacher.html')
            return HttpResponse(template.render(context, request))
    else:
        form = AssignStudentToTeacherForm()
        context = {
            "form": form,
        }
        template = loader.get_template('stuff/assign_student_to_teacher.html')
        return HttpResponse(template.render(context, request))


@login_required
def reject_stud_to_teach(request, teacher_id):
    if request.method == 'POST':
        form_data = RejectStudentToTeacherForm(data=request.POST, teacher_id=teacher_id)
        if form_data.is_valid():
            student = form_data.cleaned_data['subject_to_delete']
            student.delete()
            return HttpResponse('Успешно удалено')
        else:
            context = {
                "form": form_data
            }
            template = loader.get_template('stuff/reject_student_to_teacher.html')
            return HttpResponse(template.render(context, request))
    else:
        form = RejectStudentToTeacherForm(teacher_id=teacher_id)
        context = {
            "form": form
        }
        template = loader.get_template('stuff/reject_student_to_teacher.html')
        return HttpResponse(template.render(context, request))


@login_required
def set_available_timestamps(request, teacher_id):
    context = {}
    template = loader.get_template('stuff/set_available_timestamps.html')
    return HttpResponse(template.render(context,request))


# Student section
@login_required
def get_student_list(request):
    students = Student.objects.filter(rmv=False)
    context = {
        "students": students,
    }
    template = loader.get_template('stuff/student_list.html')
    return HttpResponse(template.render(context, request))


@login_required
def get_student_archive_list(request):
    students = Student.objects.filter(rmv=True)
    context = {
        "students": students
    }
    template = loader.get_template('stuff/student_list.html')
    return HttpResponse(template.render(context, request))


@login_required
def get_filtered_student_list(request):
    req = request.GET['req']
    students = Student.objects.filter(first_name__icontains=req, rmv=False) | \
        Student.objects.filter(last_name__icontains=req, rmv=False)
    context = {
        "students": students,
    }
    template = loader.get_template('stuff/student_list.html')
    return HttpResponse(template.render(context, request))


@login_required
def student_details(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    context = {"student": student}
    return render(request, 'stuff/student.html', context=context)


@login_required
def add_student(request):
    if request.method == 'POST':
        form_data = AddStudentForm(data=request.POST)
        if form_data.is_valid():
            new_student = form_data.save()
            return HttpResponse('Сохранено успешно', status='201')
        else:
            context = {
                "form": form_data,
            }
            template = loader.get_template('stuff/add_student.html')
            return HttpResponse(template.render(context, request))
    else:
        form = AddStudentForm()
        context = {
            "form": form,
        }
        template = loader.get_template('stuff/add_student.html')
        return HttpResponse(template.render(context, request))


@login_required
def delete_student(request, student_id):
    if request.method == 'POST':
        student = get_object_or_404(Student, pk=student_id)
        student.delete()
        return HttpResponse('Запись удалена')


@login_required
def archive_student(request, student_id):
    if request.method == 'POST':
        student = get_object_or_404(Student, pk=student_id)
        if student.rmv:
            student.rmv = False
            student.save()
            return HttpResponse('Перенесено из Архива')
        else:
            student.rmv = True
            student.save()
            return HttpResponse('Занесено в Архив')


@login_required
def classes_per_day(request, teacher_id, year, month, day):
    d = date(year, month, day)
    events = SubjectClass.objects.filter(subject__teacher=teacher_id, day=d.weekday())
    timestamps = AvailableTimestamp.objects.filter(teacher=teacher_id, day=d.weekday())
    extra_classes_canceled = ExtraClass.objects.filter(subject__teacher=teacher_id, moved_from_date=d)
    extra_classes_added = ExtraClass.objects.filter(subject__teacher=teacher_id, moved_to_date=d)
    scheduled_day = ''
    for hour in range(0, 24):
        for minute in range(0, 60, 10):
            t = time(hour=hour, minute=minute)
            events_per_time = events.filter(start_time=t)
            timestamp_per_time = timestamps.filter(start_time=t)
            canceled_classes_per_time = extra_classes_canceled.filter(moved_from_start_time=t)
            added_classes_per_time = extra_classes_added.filter(moved_to_start_time=t)

            if added_classes_per_time:
                for cls in added_classes_per_time:
                    scheduled_day += f'<tr class="success"><td>{cls.moved_to_start_time}</td>' \
                                     f'<td>{cls.subject.student}</td>' \
                                     f'<td>{cls.subject.subject}</td>' \
                                     f'<td>Добавлен</td></tr>'
            elif canceled_classes_per_time:
                for cls in canceled_classes_per_time:
                    scheduled_day += f'<tr class="warning"><td>{cls.moved_from_start_time}</td>' \
                                     f'<td>{cls.subject.student}</td>' \
                                     f'<td>{cls.subject.subject}</td>' \
                                     f'<td>Отменен</td></tr>'
            elif events_per_time:
                for event in events_per_time:
                    scheduled_day += f'<tr><td>{event.start_time}</td>' \
                                     f'<td>{event.subject.student}</td>' \
                                     f'<td>{event.subject.subject}</td>' \
                                     f'<td>По расписанию</td></tr>'
            elif timestamp_per_time:
                for timestamp in timestamp_per_time:
                    scheduled_day += f'<tr class="info"><td>{timestamp.start_time}</td>' \
                                     f'<td></td>' \
                                     f'<td></td>' \
                                     f'<td>Занятия нет</td></tr>'
    scheduled_day_html = mark_safe(scheduled_day)
    context = {
        "scheduled_day": scheduled_day_html,
        "d": d,
    }
    template = loader.get_template('stuff/classes_per_day.html')
    return HttpResponse(template.render(context, request))


def get_date():
    return datetime.today()


def get_future_date(delta):
    return get_date() + timedelta(days=delta)
