from django.http import JsonResponse
from django.views import View
from django.core.serializers import serialize
from .models import Student, Teacher, Subject


class StudentsList(View):
    def get(self, request):
        students_count = Student.objects.count()
        students = Student.objects.all()
        students_list = serialize('python', students, ensure_ascii=False)
        data = {
            "students": students_list,
            "count": students_count
        }
        return JsonResponse(data=data)


class StudentDetails(View):
    def get(self, request, student_id):
        student = Student.objects.get(pk=student_id)
        data = serialize('python', [student])
        return JsonResponse(data=data)
