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


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


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
