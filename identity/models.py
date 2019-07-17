from django.contrib.auth.models import AbstractUser
from django.db import models
from hs_infra.entities.base.base_entity import BaseModel

from university.models import Faculty, Course, StudentCard, StudyField
from .enums import EduTypeEnum


class User(AbstractUser):
    code = models.CharField(max_length=30, null=False)
    study_field = models.ForeignKey(StudyField, on_delete=models.CASCADE)


class UniversityUser(User):
    class Meta:
        abstract = True


class Student(BaseModel):
    entrance = models.BigIntegerField()
    education_type = models.IntegerField(choices=EduTypeEnum.choices(), default=EduTypeEnum.Day.value)

    student_cards = models.ManyToManyField(StudentCard)
    courses = models.ManyToManyField(Course, blank=True, null=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        related_name="student",
        related_query_name="student",
    )


class Teacher(BaseModel):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, blank=True, null=True)
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        related_name="teacher",
        related_query_name="teacher",
    )

    def __str__(self):
        return self.user.username
