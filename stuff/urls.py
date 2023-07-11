from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('student/<int:student_id>/', views.student_details, name='student_details'),
    path('teacher/<int:teacher_id>', views.teacher_details, name='teacher_details'),
]