from django.contrib import admin
from django.contrib.auth.models import User
from .models import *


class IdentityAdmin(admin.ModelAdmin):
	list_display = ('user',)

class StudentAdmin(IdentityAdmin):
	pass

class TeacherAdmin(IdentityAdmin):
	pass




admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)

