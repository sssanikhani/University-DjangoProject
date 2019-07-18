from rest_framework import serializers
from identity.serializers import *
from .models import *
from .enums import TermEnum


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


class StudyFieldsListSerializer(serializers.ModelSerializer):
	class Meta:
		model = StudyField
		fields = ('id', 'title',)


class CoursesListSerializer(serializers.ModelSerializer):
	faculty = FacultiesListSerializer()
	study_field = StudyFieldsListSerializer()
	class Meta:
		model = Course
		fields = ('id', 'title', 'code', 'faculty', 'study_field',)


class CoursesListBriefSerializer(serializers.ModelSerializer):
	study_field = StudyFieldsListSerializer()
	class Meta:
		model = Course
		fields = ('id', 'title', 'code', 'study_field')


class CoursesListBriefNoStudyFieldSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = ('id', 'title', 'code',)


class StudyFieldInfoSerializer(serializers.ModelSerializer):
	course_set = CoursesListBriefNoStudyFieldSerializer(many=True)
	studyfield_set = StudyFieldsListSerializer(many=True)
	parent = StudyFieldsListSerializer()
	class Meta:
		model = StudyField
		exclude = ('created_at', 'updated_at',)


class CourseInfoSerializer(serializers.ModelSerializer):
	teacher_set = TeacherListSerializer(many=True)
	faculty = FacultiesBriefSerializer()
	study_field = StudyFieldsListSerializer()
	class Meta:
		model = Course
		exclude = ('created_at', 'updated_at',)


class FacultyInfoSerializer(serializers.ModelSerializer):
	course_set = CoursesListBriefSerializer(many = True)
	university = UniversitiesBriefSerializer()
	class Meta:
		model = Faculty
		exclude = ('created_at', 'updated_at',)


class UniversityInfoSerializer(serializers.ModelSerializer):
	faculty_set = FacultiesBriefSerializer(many = True)
	class Meta:
		model = University
		exclude = ('created_at', 'updated_at',)