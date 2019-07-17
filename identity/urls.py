from django.urls import path
from .views import *

app_name = "identity"

urlpatterns = [
	path('students/signup/', SignupStudent.as_view(), name = "signup_student"),
	path('teachers/signup/', SignupTeacher.as_view(), name = "signup_teacher"),
	path('teachers/all/', TeachersList.as_view(), name = "all_teachers"),
	path('students/all/', StudentsList.as_view(), name = "all_students"),
	path('profile/', Profile.as_view(), name = 'profile'),
]