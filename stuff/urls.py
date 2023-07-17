from django.urls import path
from . import views
from .api import StudentsList, StudentDetails, TeachersList, TeacherDetails


views_patterns = [
    path('', views.index, name='index'),
    path('student/<int:student_id>/', views.student_details, name='student_details'),
    path('teacher/<int:teacher_id>', views.teacher_details, name='teacher_details'),
]
api_patterns = [

    path('student/list', StudentsList.as_view()),
    path('student/<int:id>', StudentDetails.as_view()),
    path('teacher/list', TeachersList.as_view()),
    path('teacher/<int:id>', TeacherDetails.as_view()),
]
