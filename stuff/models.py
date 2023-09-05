from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=20, null=True, blank=True, verbose_name='Фамилия')
    contact = models.CharField(max_length=15, null=True, blank=True, verbose_name='Контакт студента')
    birthday = models.DateField(null=True, blank=True, verbose_name='День рождения')
    is_adult = models.BooleanField(verbose_name="Взрослый", default=False)
    rmv = models.BooleanField(verbose_name='Архивный', default=False)
    parent_first_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Имя родителя')
    parent_last_name = models.CharField(max_length=20, null=True, blank=True, verbose_name='Фамилия родителя')
    parent_contact = models.CharField(max_length=15, null=True, blank=True, verbose_name='Контакт родителя')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class SubjectList(models.Model):
    subject_list_item = models.CharField(max_length=20, verbose_name='Предмет')

    def __str__(self):
        return self.subject_list_item


class Teacher(models.Model):
    first_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Фамилия')
    contact = models.CharField(max_length=15, null=True, blank=True, verbose_name='Контакт')
    birthday = models.DateField(null=True, blank=True, verbose_name='День рождения')
    rmv = models.BooleanField(verbose_name='Архивный', default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Subject(models.Model):
    student = models.ForeignKey(to='Student', on_delete=models.CASCADE, null=True, blank=True,
                                verbose_name='Студент')
    teacher = models.ForeignKey(to='Teacher', on_delete=models.CASCADE, null=True, blank=True,
                                verbose_name='Преподаватель')
    subject = models.ForeignKey(to='SubjectList', on_delete=models.CASCADE, null=True, blank=True,
                                verbose_name='Предмет')

    def __str__(self):
        return f"{self.student} {self.teacher} {self.subject}"


class SubjectClass(models.Model):
    days = (
        (0, 'ПН'),
        (1, 'ВТ'),
        (2, 'СР'),
        (3, 'ЧТ'),
        (4, 'ПТ'),
        (5, 'СБ'),
        (6, 'ВС')
    )
    subject = models.ForeignKey(to='Subject', on_delete=models.CASCADE)
    day = models.SmallIntegerField(choices=days, verbose_name='Дата')
    start_time = models.TimeField(verbose_name='Время начала')

    def __str__(self):
        return f"{self.subject} {self.day} {self.start_time}"


class ExtraClass(models.Model):
    subject = models.ForeignKey(to='Subject', on_delete=models.CASCADE)
    statuses = (
        (-1, 'Отменен'),
        (1, 'Добавлен'),
        (0, 'Перенесен')
    )
    status = models.SmallIntegerField(choices=statuses, verbose_name='Статус')
    moved_from_date = models.DateField(null=True, blank=True, verbose_name='Дата')
    moved_from_start_time = models.TimeField(null=True, blank=True, verbose_name='Время начала')
    moved_to_date = models.DateField(null=True, blank=True, verbose_name='Дата')
    moved_to_start_time = models.TimeField(null=True, blank=True, verbose_name='Время начала')


class AvailableTimestamp(models.Model):
    days = (
        (0, 'ПН'),
        (1, 'ВТ'),
        (2, 'СР'),
        (3, 'ЧТ'),
        (4, 'ПТ'),
        (5, 'СБ'),
        (6, 'ВС')
    )
    teacher = models.ForeignKey(to='Teacher', on_delete=models.CASCADE)
    day = models.SmallIntegerField(choices=days)
    start_time = models.TimeField()

    def __str__(self):
        return f'{self.teacher} {self.day} {self.start_time}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
