from django import forms
from .models import Teacher, Student, Subject, SubjectList


class ModelSelectForRejectStud(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.student} {obj.subject}"


class AddTeacherForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя', max_length=30, required=True,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label='Фамилия', max_length=30, required=True,
                                widget=forms.TextInput(attrs={"class": "form-control"}))
    contact = forms.CharField(label='Контакт', max_length=15, required=False,
                              widget=forms.TextInput(attrs={"class": "form-control"}))
    birthday = forms.DateField(label='День рождения', input_formats='%d.%m.%Y', required=False,
                               error_messages={'required': 'Обязательное поле.',
                                               'invalid': 'Введите дату в формате ДД.ММ.ГГГГ'},
                               widget=forms.DateInput(format='%d.%m.%Y', attrs={"class": "form-control"}))

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'contact', 'birthday']


class AssignStudentToTeacherForm(forms.ModelForm):
    student = forms.ModelChoiceField(queryset=Student.objects.filter(rmv=False), label='Студент',
                                     widget=forms.Select(attrs={"class": "form-control"}))
    subject = forms.ModelChoiceField(queryset=SubjectList.objects.all(), label='Предмет',
                                     widget=forms.Select(attrs={"class": "form-control"}))

    class Meta:
        model = Subject
        fields = ['student', 'subject']


class RejectStudentToTeacherForm(forms.ModelForm):
    def __init__(self, teacher_id, *args, **kwargs):
        self.teacher_id = teacher_id
        super().__init__(*args, **kwargs)
        subjects = Subject.objects.filter(teacher__pk=teacher_id)
        self.fields['subject_to_delete'].queryset = subjects

    subject_to_delete = ModelSelectForRejectStud(queryset=Subject.objects.all(), label='Студент',
                                       widget=forms.Select(attrs={"class": "form-control"}))

    class Meta:
        model = Subject
        fields = ['subject_to_delete']


class AddStudentForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя', max_length=30, required=True,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label='Фамилия', max_length=30, required=False,
                                widget=forms.TextInput(attrs={"class": "form-control"}))
    contact = forms.CharField(label='Контакт', max_length=15, required=False,
                              widget=forms.TextInput(attrs={"class": "form-control"}))
    birthday = forms.DateField(label='День рождения', required=False, input_formats='%d.%m.%Y',
                               error_messages={'required': 'Обязательное поле',
                                               'invalid': 'Введите дату в формате ДД.ММ.ГГГГ'},
                               widget=forms.DateInput(format='%d.%m.%Y', attrs={"class": "form-control"}))
    is_adult = forms.BooleanField(label='Взрослый', required=False,
                                  widget=forms.CheckboxInput())
    parent_first_name = forms.CharField(label='Имя родителя', max_length=30, required=False,
                                        widget=forms.TextInput(attrs={"class": "form-control"}))
    parent_last_name = forms.CharField(max_length=30, label='Фамилия родителя', required=False,
                                       widget=forms.TextInput(attrs={"class": "form-control"}))
    parent_contact = forms.CharField(max_length=15, label='Контакт родителя', required=False,
                                     widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'contact', 'birthday', 'is_adult', 'parent_first_name',
                  'parent_last_name', 'parent_contact']
