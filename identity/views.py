from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework import generics
from .models import *

def create_user(request, serializer):
	user_serializer = UserCreateSerializer(data = request.data.get('user'))
	if user_serializer.is_valid():
		user = user_serializer.save(is_staff = True)
	else:
		return user_serializer.errors
	serializer.save(user=user)
	return True


class SignupStudent(APIView):
	def post(self, request):
		serializer = StudentSignupSerializer(data = request.data)
		if not serializer.is_valid():
			return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
		user_status = create_user(request, serializer)
		if user_status == True:
			return Response(status = status.HTTP_201_CREATED)
		else:
			return Response(user_status, status.HTTP_400_BAD_REQUEST)
		return Response(status = status.HTTP_201_CREATED)

class SignupTeacher(APIView):
	def post(self, request):
		serializer = TeacherSignupSerializer(data = request.data)

		if not serializer.is_valid():
			return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
		user_status = create_user(request, serializer)
		if user_status == True:
			return Response(status = status.HTTP_201_CREATED)
		else:
			return Response(user_status, status.HTTP_400_BAD_REQUEST)


class Profile(APIView):
	def get(self, request):
		if request.user.is_anonymous:
			return Response(status=status.HTTP_401_UNAUTHORIZED)

		if hasattr(request.user, 'student'):
			serializer = StudentProfileSerializer(request.user.student)
		elif hasattr(request.user, 'teacher'):
			serializer = TeacherProfileSerializer(request.user.teacher)
		else:
			serializer = UserSerializer(request.user)

		return Response(serializer.data, status = status.HTTP_200_OK)


class StudentsList(generics.ListAPIView):
	serializer_class = StudentListSerializer
	queryset = Student.objects.all()


class TeachersList(generics.ListAPIView):
	serializer_class = TeacherListSerializer
	queryset = Teacher.objects.all()