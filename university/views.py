from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

class CoursesList(generics.ListAPIView):
	serializer_class = CoursesListSerializer
	queryset = Course.objects.all()

class CourseInfo(generics.RetrieveAPIView):
	serializer_class = CourseInfoSerializer
	queryset = Course.objects.all()
	lookup_field = 'id'

class FacultiesList(generics.ListAPIView):
	serializer_class = FacultiesListSerializer
	queryset = Faculty.objects.all()

class FacultyInfo(generics.RetrieveAPIView):
	serializer_class = FacultyInfoSerializer
	queryset = Faculty.objects.all()
	lookup_field = 'id'

class UniversitiesList(generics.ListAPIView):
	serializer_class = UniversitiesListSerializer
	queryset = University.objects.all()

class UniversityInfo(generics.RetrieveAPIView):
	serializer_class = UniversityInfoSerializer
	queryset = University.objects.all()
	lookup_field = 'id'
