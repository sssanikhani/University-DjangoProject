from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import *

admin.site.register(BaseUser)


class IdentityAdmin(admin.ModelAdmin):
    list_display = ('user',)


class StudentAdmin(IdentityAdmin):
    pass


admin.site.unregister(Group)
admin.site.register(BaseUser)

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
