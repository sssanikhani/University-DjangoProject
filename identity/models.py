from django.db import models
from django.contrib.auth.models import User
from university.models import Faculty, Course, StudentCard
from .enums import EduTypeEnum

class Student(models.Model):
	code = models.CharField(max_length = 30, null = False)
	entrance = models.BigIntegerField(null = True, blank = True)
	education_type = models.CharField(max_length = 30, choices = EduTypeEnum.choices(), default = EduTypeEnum.Day.value)
	active_type = models.BooleanField(default = True)
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30, null = True, blank = True)
	
	student_cards = models.ManyToManyField(StudentCard)
	courses = models.ManyToManyField(Course, blank = True, null = True)
	faculty = models.ForeignKey(Faculty, on_delete = models.CASCADE)
	user = models.OneToOneField(User, related_name = "student", on_delete = models.CASCADE)

	def __str__(self):
		return self.user.username


class Teacher(models.Model):
	code = models.CharField(max_length = 30, null = False)
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30, null = True, blank = True)

	faculty = models.ForeignKey(Faculty, on_delete = models.CASCADE)
	courses = models.ManyToManyField(Course, blank = True, null = True)
	user = models.OneToOneField(User, related_name = "teacher", on_delete = models.CASCADE)

	def __str__(self):
		return self.user.username