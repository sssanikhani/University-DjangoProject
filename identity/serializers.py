from .models import *
from rest_framework import serializers
from .enums import EduTypeEnum

class TeacherSignupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Teacher
		exclude = ('user',)


class StudentSignupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		exclude = ('user',)


class UserCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = BaseUser
		fields = ('first_name', 'last_name', 'username', 'password', 'email',)

	def create(self, validated_data):
		return BaseUser.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = BaseUser
		fields = ('first_name', 'last_name', 'username',)


class TeacherListSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = Teacher
		fields = ('user',)


class StudentListSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = Student
		fields = ('user',)

from university.serializers import FacultiesListSerializer, CoursesListBriefSerializer

class TeacherProfileSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	faculty = FacultiesListSerializer()
	courses = CoursesListBriefSerializer(many = True)
	class Meta:
		model = Teacher
		fields = '__all__'


class StudentProfileSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	faculty = FacultiesListSerializer()
	courses = CoursesListBriefSerializer(many = True)
	class Meta:
		model = Student
		exclude = ('student_cards',)