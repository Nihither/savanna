from django.urls import path
from .views import index, get_teacher_list, get_student_list, student_details, teacher_details, person_details_view, \
    classes_per_day, add_teacher, add_student
from .api import StudentsList, StudentDetails, TeachersList, TeacherDetails, PersonView
from .scheduler import birthday_notification
from .account_views import user_login, user_logout, PasswordReset, PasswordResetDone, PasswordResetConfirm, \
    PasswordResetComplete, PasswordChange, PasswordChangeDone


# path starts with http://{host}/
views_patterns = [
    path('', index, name='index'),
    path('teacher/list/', get_teacher_list, name='teacher_list'),
    path('student/list/', get_student_list, name='student_list'),
    path('student/<int:student_id>/', student_details, name='student_details'),
    path('teacher/<int:teacher_id>/', teacher_details, name='teacher_details'),
    path('<person>/<int:person_id>/details/', person_details_view),
    path('teacher/<int:teacher_id>/<int:year>/<int:month>/<int:day>/', classes_per_day, name='classes_per_day'),
    path('teacher/add/', add_teacher, name='add_teacher'),
    path('student/add/', add_student, name='add_student')
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
    path('password_reset/', PasswordReset.as_view(), name='password_reset'),
    path('password_reset/done', PasswordResetDone.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', PasswordResetComplete.as_view(), name='password_reset_complete'),
    path('password_change/', PasswordChange.as_view(), name='password_change'),
    path('password_change/done', PasswordChangeDone.as_view(), name='password_change_done'),
]