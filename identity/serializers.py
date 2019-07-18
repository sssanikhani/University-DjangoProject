from .models import *
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
		model = BaseUser
		fields = '__all__'

	"""def create(self, validated_data):
		new_user = UniversityUser.objects.create(**validated_data)
		new_user.set_password(validated_data.get['password'])
		return new_user"""

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = BaseUser
		fields = ('id', 'username',)


class TeacherListSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = Teacher
		fields = ('first_name', 'last_name', 'user',)


class StudentListSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = Student
		fields = ('first_name', 'last_name', 'user',)

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