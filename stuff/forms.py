from django import forms
from .models import Teacher, Student, Subject, SubjectList


class AddTeacherForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя', max_length=30, required=True,
                                 widget=forms.widgets.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label='Фамилия', max_length=30, required=True,
                                widget=forms.widgets.TextInput(attrs={"class": "form-control"}))
    contact = forms.CharField(label='Контакт', max_length=15, required=False,
                              widget=forms.widgets.TextInput(attrs={"class": "form-control"}))
    birthday = forms.DateField(label='День рождения', input_formats='%d.%m.%Y', required=False,
                               error_messages={'required': 'Обязательное поле.',
                                               'invalid': 'Введите дату в формате ДД.ММ.ГГГГ'},
                               widget=forms.widgets.DateInput(format='%d.%m.%Y', attrs={"class": "form-control"}))

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'contact', 'birthday']


class AssignStudentToTeacherForm(forms.ModelForm):
    student = forms.ModelChoiceField(queryset=Student.objects.filter(rmv=False), label='Студент',
                                     widget=forms.widgets.Select(attrs={"class": "form-control"}))
    subject = forms.ModelChoiceField(queryset=SubjectList.objects.all(), label='Предмет',
                                     widget=forms.widgets.Select(attrs={"class": "form-control"}))

    class Meta:
        model = Subject
        fields = ['student', 'subject']


class AddStudentForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя', max_length=30, required=True,
                                 widget=forms.widgets.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label='Фамилия', max_length=30, required=False,
                                widget=forms.widgets.TextInput(attrs={"class": "form-control"}))
    contact = forms.CharField(label='Контакт', max_length=15, required=False,
                              widget=forms.widgets.TextInput(attrs={"class": "form-control"}))
    birthday = forms.DateField(label='День рождения', required=False, input_formats='%d.%m.%Y',
                               error_messages={'required': 'Обязательное поле',
                                               'invalid': 'Введите дату в формате ДД.ММ.ГГГГ'},
                               widget=forms.widgets.DateInput(format='%d.%m.%Y', attrs={"class": "form-control"}))
    is_adult = forms.BooleanField(label='Взрослый', required=False,
                                  widget=forms.widgets.CheckboxInput())
    parent_first_name = forms.CharField(label='Имя родителя', max_length=30, required=False,
                                        widget=forms.widgets.TextInput(attrs={"class": "form-control"}))
    parent_last_name = forms.CharField(max_length=30, label='Фамилия родителя', required=False,
                                       widget=forms.widgets.TextInput(attrs={"class": "form-control"}))
    parent_contact = forms.CharField(max_length=15, label='Контакт родителя', required=False,
                                     widget=forms.widgets.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'contact', 'birthday', 'is_adult', 'parent_first_name',
                  'parent_last_name', 'parent_contact']
