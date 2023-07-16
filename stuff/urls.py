from django.urls import path
from . import views
from .api import StudentsList, StudentDetails


urlpatterns = [
    path('', views.index, name='index'),
    path('student/<int:student_id>/', views.student_details, name='student_details'),
    path('teacher/<int:teacher_id>', views.teacher_details, name='teacher_details'),
    path('api/student/list', StudentsList.as_view()),
    path('api/student/<int:student_id>', StudentDetails.as_view()),
]