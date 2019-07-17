from rest_framework import serializers
from identity.serializers import *
from .models import *

class UniversitiesListSerializer(serializers.ModelSerializer):
	class Meta:
		model = University
		fields = ('id', 'title', 'code', 'website',)

class UniversitiesBriefSerializer(serializers.ModelSerializer):
	class Meta:
		model = University
		fields = ('id', 'title', 'code',)

class FacultiesListSerializer(serializers.ModelSerializer):
	university = UniversitiesBriefSerializer()
	class Meta:
		model = Faculty
		fields = ('id', 'title', 'code', 'website', 'university',)

class FacultiesBriefSerializer(serializers.ModelSerializer):
	class Meta:
		model = Faculty
		fields = ('id', 'title', 'code', 'website',)

class CoursesListSerializer(serializers.ModelSerializer):
	faculty = FacultiesListSerializer()
	class Meta:
		model = Course
		fields = ('id', 'title', 'code', 'faculty',)

class CoursesListBriefSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = ('id', 'title', 'code',)

class CourseInfoSerializer(serializers.ModelSerializer):
	teacher_set = TeacherListSerializer(many=True)
	faculty = FacultiesBriefSerializer()
	class Meta:
		model = Course
		fields = '__all__'

class FacultyInfoSerializer(serializers.ModelSerializer):
	course_set = CoursesListBriefSerializer(many = True)
	university = UniversitiesBriefSerializer()
	class Meta:
		model = Faculty
		fields = '__all__'

class UniversityInfoSerializer(serializers.ModelSerializer):
	faculty_set = FacultiesBriefSerializer(many = True)
	class Meta:
		model = University
		fields = '__all__'