from django.urls import path
from .views import index, student_details, teacher_details
from .api import StudentsList, StudentDetails, TeachersList, TeacherDetails, PersonView


# path starts with http://{host}/
views_patterns = [
    path('', index, name='index'),
    path('student/<int:student_id>/', student_details, name='student_details'),
    path('teacher/<int:teacher_id>', teacher_details, name='teacher_details'),
]

# path starts with http://{host}/api/
api_patterns = [
    # path('student/list', StudentsList.as_view()),
    # path('student/<int:id>', StudentDetails.as_view()),
    # path('teacher/list', TeachersList.as_view()),
    # path('teacher/<int:id>', TeacherDetails.as_view()),
    path('<person>/<int:id>/details', PersonView.as_view())
]
