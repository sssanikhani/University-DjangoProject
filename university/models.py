from django.db import models
from hs_infra.entities.base.base_entity import BaseModel

from .enums import TermEnum


class University(BaseModel):
    title = models.CharField(max_length=30, null=False)
    code = models.CharField(max_length=30, null=False)
    address = models.CharField(max_length=255, null=True)
    postal_code = models.CharField(max_length=30, null=False)
    website = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Faculty(BaseModel):
    title = models.CharField(max_length=30, null=False)
    code = models.CharField(max_length=30, null=False)
    address = models.CharField(max_length=255, null=True, blank=True)
    postal_code = models.CharField(max_length=30, null=False)
    website = models.CharField(max_length=255, null=True, blank=True)

    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Course(BaseModel):
    title = models.CharField(max_length=30, null=False)
    code = models.CharField(max_length=30, null=False)
    term = models.IntegerField(choices=TermEnum.choices(), default=TermEnum.arbitrary.value)

    faculty = models.ForeignKey(
        to=Faculty,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title


class StudentCard(BaseModel):
    code = models.CharField(max_length=30)

    def __str__(self):
        return self.code


class StudyField(BaseModel):
    title = models.CharField(max_length=100)

    parent = models.ForeignKey(
        to='StudyField',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.title
