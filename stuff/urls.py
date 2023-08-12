from django.urls import path
from .views import index, student_details, teacher_details, person_details_view
from .api import StudentsList, StudentDetails, TeachersList, TeacherDetails, PersonView
from .scheduler import birthday_notification
from .account_views import user_login, user_logout


# path starts with http://{host}/
views_patterns = [
    path('', index, name='index'),
    path('student/<int:student_id>/', student_details),
    path('teacher/<int:teacher_id>/', teacher_details),
    path('<person>/<int:person_id>/details/', person_details_view),
]

# path starts with http://{host}/api/
api_patterns = [
    path('student/list/', StudentsList.as_view()),
    path('student/<int:id>/', StudentDetails.as_view()),
    path('teacher/list/', TeachersList.as_view()),
    path('teacher/<int:id>/', TeacherDetails.as_view()),
    path('<person>/<int:person_id>/details/', PersonView.as_view()),
    path('scheduler/', birthday_notification),
]

# path starts with account
accounts_patterns = [
    path('login/', user_login, name='login'),
    path('logout/next=<path:next>', user_logout, name='logout'),
]