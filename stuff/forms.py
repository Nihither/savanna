from django import forms
from.models import Teacher


class AddTeacherForm(forms.ModelForm):
    first_name = forms.CharField(required=True, label='Имя',
                                 widget=forms.widgets.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(required=True, label='Фамилия',
                                widget=forms.widgets.TextInput(attrs={"class": "form-control"}))
    contact = forms.CharField(required=False, label='Контакт',
                              widget=forms.widgets.TextInput(attrs={"class": "form-control"}))
    birthday = forms.DateField(required=False, label='День рождения',
                               error_messages={'required': 'Обязательное поле.', 'invalid': 'Введите дату в формате ДД.ММ.ГГГГ'},
                               widget=forms.widgets.DateInput(format='%d.%m.%Y', attrs={"class": "form-control"}))

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'contact', 'birthday']
