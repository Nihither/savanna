from django.http import JsonResponse
from django.views import View
from django.core.serializers import serialize
from .models import Student, Teacher, Subject


class StudentsList(View):
    def get(self, request):
        students_count = Student.objects.count()
        students_list = Student.objects.all()
        students = serialize('python', students_list)
        data = {
            "students": students,
            "count": students_count
        }
        return JsonResponse(data=data)


class StudentDetails(View):
    def get(self, request, id):
        student = Student.objects.get(pk=id)
        data = {
            "id": student.pk,
            "first_name": student.first_name,
            "last_name": student.last_name,
            "contact": student.contact,
            "birthday": student.birthday
        }
        return JsonResponse(data=data)


class TeachersList(View):
    def get(self, request):
        teachers_list = Teacher.objects.all()
        teachers_count = Teacher. objects.count()
        teachers = serialize('python', teachers_list)
        data = {
            "teachers": teachers,
            "count": teachers_count
        }
        return JsonResponse(data=data)


class TeacherDetails(View):
    def get(self, request, id):
        teacher = Teacher.objects.get(pk=id)
        data = {
            "id": teacher.pk,
            "first_name": teacher.first_name,
            "last_name": teacher.last_name,
            "contact": teacher.contact,
            "birthday": teacher.birthday
        }
        return JsonResponse(data)


class PersonView(View):
    def get(self, request, person, person_id):
        if person == 'student':
            student = Student.objects.get(pk=person_id)
            subjects = Subject.objects.filter(student=person_id)
            subjects_serialized = serialize('python', subjects)
            data = {
                "id": student.pk,
                "first_name": student.first_name,
                "last_name": student.last_name,
                "contact": student.contact,
                "birthday": student.birthday,
                "subjects": subjects_serialized
            }
            return JsonResponse(data=data)
        elif person == 'teacher':
            teacher = Teacher.objects.get(pk=person_id)
            subjects = Subject.objects.filter(teacher=person_id)
            subjects_serialized = serialize('python', subjects)
            data = {
                "id": teacher.pk,
                "first_name": teacher.first_name,
                "last_name": teacher.last_name,
                "contact": teacher.contact,
                "birthday": teacher.birthday,
                "subjects": subjects_serialized
            }
            return JsonResponse(data=data)