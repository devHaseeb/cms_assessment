from rest_framework import viewsets, generics
from core.models import Student, School
from apis.serializers import StudentSerializer, SchoolSerializer, LogEntrySerializer
from django.conf import settings
from django.shortcuts import redirect
from auditlog.models import LogEntry
from rest_framework.response import Response
import json


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    
    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        location = self.request.query_params.get('location', None)
        max_students = self.request.query_params.get('max_students', None)
        
        queryset = self.queryset
        if name is not None:
            queryset = queryset.filter(name__iexact=name)
        if location is not None:
            queryset = queryset.filter(location__iexact=location)
        if max_students is not None:
            queryset = queryset.filter(max_students__gt=max_students)
        return queryset


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get_queryset(self):
        age = self.request.query_params.get('age', None)
        nationality = self.request.query_params.get('nationality', None)
        location = self.request.query_params.get('location', None)
        student_id = self.request.query_params.get('student_id', None)
        
        queryset = self.queryset
        if age is not None:
            queryset = queryset.filter(age__gt=age)
        if nationality is not None:
            queryset = queryset.filter(nationality__iexact=nationality)
        if location is not None:
            queryset = queryset.filter(location__iexact=location)
        if student_id is not None:
            queryset = queryset.filter(student_id__iexact=student_id)
        return queryset
    
    def list(self, request, school_pk=None):
        queryset = self.queryset.filter(school_id=school_pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class LogEntryViewSet(viewsets.ModelViewSet):
    queryset = LogEntry.objects.all()
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        results = []
        for log_entry in queryset:
            print(log_entry)
            changes = json.loads(log_entry.changes)
            for key, value in changes.items():
                if value[0] != "None":
                    data = key+" " + value[0]+" was edited to "+value[1] + \
                        " at "+str((log_entry.timestamp).strftime('%c'))
                    results.append(data)

        return Response({"results": results})
    serializer_class = LogEntrySerializer
