from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    contact = models.CharField(max_length=15, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    parent_first_name = models.CharField(max_length=30, null=True, blank=True)
    parent_last_name = models.CharField(max_length=20, null=True, blank=True)
    parent_contact = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class SubjectList(models.Model):
    subject_list_item = models.CharField(max_length=20)

    def __str__(self):
        return self.subject_list_item


class Teacher(models.Model):
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    contact = models.CharField(max_length=15, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    subject_list_item = models.ManyToManyField(to='SubjectList')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Subject(models.Model):
    student = models.ForeignKey(to='Student', on_delete=models.CASCADE, null=True, blank=True)
    teacher = models.ForeignKey(to='Teacher', on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey(to='SubjectList', on_delete=models.CASCADE, null=True, blank=True)
    paid_classes = models.SmallIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.student} {self.teacher} {self.subject}"


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

