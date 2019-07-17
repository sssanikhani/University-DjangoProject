from django.contrib import admin
from django.contrib.auth.models import User
from .models import *


class IdentityAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'code',)

class StudentAdmin(IdentityAdmin):
	pass

class TeacherAdmin(IdentityAdmin):
	pass



# admin.site.unregister(User)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)

