from django.shortcuts import render
from .models import Student, Teacher, Subject


# Create your views here.

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
