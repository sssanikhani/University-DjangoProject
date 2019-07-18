from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import *


class IdentityAdmin(admin.ModelAdmin):
	list_display = ('user',)

class StudentAdmin(IdentityAdmin):
	pass

class TeacherAdmin(IdentityAdmin):
	pass


admin.site.unregister(Group)
admin.site.register(BaseUser)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)

