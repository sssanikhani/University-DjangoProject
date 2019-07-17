from django.db import models
from .enums import TermEnum

class University(models.Model):
	title = models.CharField(max_length = 30, null = False)
	code = models.CharField(max_length = 30, null = False)
	address = models.CharField(max_length = 255, null = True)
	postal_code = models.CharField(max_length = 30, null = False)
	website = models.CharField(max_length = 255)

	def __str__(self):
		return self.title

class Faculty(models.Model):
	title = models.CharField(max_length = 30, null = False)
	code = models.CharField(max_length = 30, null = False)
	address = models.CharField(max_length = 255, null = True)
	postal_code = models.CharField(max_length = 30, null = False)
	website = models.CharField(max_length = 255)

	university = models.ForeignKey(University, on_delete = models.CASCADE)

	def __str__(self):
		return self.title


class Course(models.Model):
	title = models.CharField(max_length = 30, null = False)
	code = models.CharField(max_length = 30, null = False)
	term = models.IntegerField(choices = TermEnum.choices(), default = TermEnum.term_1.value)

	faculty = models.ForeignKey(Faculty, on_delete = models.CASCADE)

	def __str__(self):
		return self.title

class StudentCard(models.Model):
	code = models.CharField(max_length = 30)

	def __str__(self):
		return self.code