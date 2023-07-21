from django.shortcuts import render, HttpResponse, get_object_or_404
from django.template import loader
from django.core.serializers import serialize
from .models import Student, Teacher, Subject


# Index view
def index(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    subjects = Subject.objects.all()
    context_dict = {
        "students": students,
        "teachers": teachers,
        "subjects": subjects
    }
    return render(request, 'stuff/index.html', context=context_dict)


# Student details vire
def student_details(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    context = {"student": student}
    return render(request, 'stuff/student.html', context=context)


# Teacher details view
def teacher_details(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    context = {"teacher": teacher}
    return render(request, 'stuff/teacher.html', context=context)


# person details view
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

