from django.contrib import admin
from .models import Student, Teacher, Subject, SubjectList, SubjectClass, ExtraClass, UserProfile, AvailableTimestamp


# Register your models here.

class SubjectInLine(admin.StackedInline):
    model = Subject


class SubjectClassInLine(admin.StackedInline):
    model = SubjectClass


class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'contact', 'birthday', 'rmv']
    ordering = ['first_name']
    inlines = [SubjectInLine]


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'contact', 'birthday', 'rmv']
    ordering = ['first_name']
    inlines = [SubjectInLine]


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['student', 'teacher', 'subject']
    ordering = ['student']
    inlines = [SubjectClassInLine]


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(SubjectList)
admin.site.register(UserProfile)
admin.site.register(SubjectClass)
admin.site.register(ExtraClass)
admin.site.register(AvailableTimestamp)
