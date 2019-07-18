from django.contrib import admin

from .models import *

admin.site.register(BaseUser)


class IdentityAdmin(admin.ModelAdmin):
    list_display = ('user',)


class StudentAdmin(IdentityAdmin):
    pass


class TeacherAdmin(IdentityAdmin):
    pass


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
