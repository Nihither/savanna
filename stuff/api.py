from django.http import JsonResponse, HttpResponse
from django.views import View
from django.core.serializers import serialize
from django.forms import model_to_dict
from .models import Student, Teacher, Subject


class StudentsList(View):
    def get(self, request):
        students_count = Student.objects.count()
        students = Student.objects.all()
        students_list = serialize('python', students)
        data = {
            "students": students_list,
            "count": students_count
        }
        return JsonResponse(data=data)


class StudentDetails(View):
    def get(self, request):
        student = Student.objects.get(pk=4)
        data = {
            "id": student.pk,
            "first_name": student.first_name,
            "last_name": student.last_name,
            "contact": student.contact,
            "birthday": student.birthday
        }
        return JsonResponse(data=data)
