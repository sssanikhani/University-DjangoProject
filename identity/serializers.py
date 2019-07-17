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

class StudentProfileSerializer(serializers.ModelSerializer):
	user = serializers.ReadOnlyField(source = 'user.username')
	faculty = serializers.ReadOnlyField(source = 'faculty.title')
	courses = serializers.StringRelatedField(many = True)
	class Meta:
		model = Student
		exclude = ('student_cards',)

class TeacherProfileSerializer(serializers.ModelSerializer):
	user = serializers.ReadOnlyField(source = 'user.username')
	faculty = serializers.ReadOnlyField(source = 'faculty.title')
	courses = serializers.StringRelatedField(many = True)
	class Meta:
		model = Teacher
		fields = '__all__'

class TeacherListSerializer(serializers.ModelSerializer):
	user = serializers.ReadOnlyField(source = 'user.username')
	class Meta:
		model = Teacher
		fields = ('first_name','last_name', 'user',)

class StudentListSerializer(serializers.ModelSerializer):
	user = serializers.ReadOnlyField(source = 'user.username')
	class Meta:
		model = Student
		fields = ('user',)