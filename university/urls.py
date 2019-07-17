from django.urls import path
from .views import *

app_name = "university"

urlpatterns = [
	path('courses/all/', CoursesList.as_view(), name = "all_courses"),
	path('courses/<int:id>/', CourseInfo.as_view(), name = "course_info"),
	path('faculties/all/', FacultiesList.as_view(), name = "all_faculties"),
	path('faculties/<int:id>/', FacultyInfo.as_view(), name = "faculty_info"),
	path('universities/all/', UniversitiesList.as_view(), name = "all_universities"),
	path('universities/<int:id>/', UniversityInfo.as_view(), name = "university_info"),
]