from django.contrib import admin
from .models import Student, Teacher, Subject, SubjectList, Event


# Register your models here.

class SubjectInLine(admin.StackedInline):
    model = Subject


class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'contact', 'birthday']
    ordering = ['first_name']
    inlines = [SubjectInLine]


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'contact', 'birthday']
    ordering = ['first_name']
    inlines = [SubjectInLine]


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['student', 'teacher', 'subject', 'paid_classes']
    ordering = ['student']


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(SubjectList)
admin.site.register(Event)
