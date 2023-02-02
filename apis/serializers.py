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
    class Meta:
        model = Student
        fields = ['id', 'uuid', 'first_name', 'last_name', 'nationality',
                  'age', 'location', 'student_id', 'school', 'created_at', 'updated_at']

    def validate(self, data):
        school = data.get('school', None)
        if school and school.max_students <= school.student_set.count():
            raise serializers.ValidationError('The selected school is full')
        return data

class LogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEntry
        fields = '__all__'
