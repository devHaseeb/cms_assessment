from rest_framework import viewsets
from core.models import Student, School
from apis.serializers import StudentSerializer, SchoolSerializer
from django.conf import settings
from django.shortcuts import redirect

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    