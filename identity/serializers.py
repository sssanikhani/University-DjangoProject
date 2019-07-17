from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers

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
		model = User
		fields = ('username', 'password', 'is_staff',)

	def create(self, validated_data):
		return User.objects.create_user(**validated_data)

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username',)

class TeacherListSerializer(serializers.ModelSerializer):
	user = serializers.ReadOnlyField(source = 'user.username')
	class Meta:
		model = Teacher
		fields = ('first_name','last_name', 'user',)

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

class StudentListSerializer(serializers.ModelSerializer):
	user = serializers.ReadOnlyField(source = 'user.username')
	class Meta:
		model = Student
		fields = ('first_name', 'last_name', 'user',)