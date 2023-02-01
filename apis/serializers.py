from rest_framework import serializers
from core.models import Student, School
import random
import string

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
    
    def validate(self, data):
        school = data.get('school', None)
        if school and school.max_students <= school.student_set.count():
            raise serializers.ValidationError('The selected school is full')
        return data

    # def create(self, validated_data):
    #     student_id = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    #     validated_data['student_id'] = student_id
    #     return super().create(validated_data)
    