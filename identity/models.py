from django.contrib.auth.models import AbstractUser
from django.db import models
from hs_infra.entities.base.base_entity import BaseModel

from university.models import Faculty, Course, StudentCard, StudyField
from .enums import EduTypeEnum


class BaseUser(AbstractUser):
    pass


class UniversityUser(BaseModel):
    code = models.CharField(max_length=30, null=False)
    # study_field = models.ForeignKey(StudyField, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, blank=True, null=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Student(UniversityUser):
    entrance = models.BigIntegerField()
    education_type = models.IntegerField(choices=EduTypeEnum.choices(), default=EduTypeEnum.Day.value)

    student_cards = models.ManyToManyField(StudentCard)
    user = models.OneToOneField(
        to=BaseUser,
        on_delete=models.CASCADE,
        related_name="student",
        related_query_name="student"
    )

    def __str__(self):
        return self.user.username


class Teacher(UniversityUser):
    user = models.OneToOneField(
        to=BaseUser,
        on_delete=models.CASCADE,
        related_name="teacher",
        related_query_name="teacher",
    )

    def __str__(self):
        return self.user.username
