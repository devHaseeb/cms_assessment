from rest_framework import serializers
from core.models import Student, School
import random
import string
from auditlog.models import LogEntry

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    school = SchoolSerializer()
    class Meta:
        model = Student
        fields = ['id', 'uuid', 'first_name', 'last_name', 'nationality', 'age', 'location', 'student_id', 'school','created_at','updated_at']
    
    def validate(self, data):
        school = data.get('school', None)
        if school and school.max_students <= school.student_set.count():
            raise serializers.ValidationError('The selected school is full')
        return data
    
    def get_queryset(self):
        queryset = Student.objects.all()
        age = self.request.query_params.get('age', None)
        nationality = self.request.query_params.get('nationality', None)
        location = self.request.query_params.get('location', None)
        student_id = self.request.query_params.get('student_id', None)

        if age is not None:
            queryset = queryset.filter(age__gt=age)
        if nationality is not None:
            queryset = queryset.filter(nationality__iexact=nationality)
        if location is not None:
            queryset = queryset.filter(location__iexact=location)
        if student_id is not None:
            queryset = queryset.filter(student_id__iexact=student_id)
        return queryset

class LogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEntry
        fields = '__all__'
    