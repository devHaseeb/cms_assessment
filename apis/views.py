from rest_framework import viewsets,generics
from core.models import Student, School
from apis.serializers import StudentSerializer, SchoolSerializer,LogEntrySerializer
from django.conf import settings
from django.shortcuts import redirect
from auditlog.models import LogEntry
from rest_framework.response import Response

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class LogEntryViewSet(viewsets.ModelViewSet):
    queryset = LogEntry.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        results = []
        for log_entry in queryset:
            data = {
                "action": log_entry.action,
                "object_repr": log_entry.object_repr,
                "object_id": log_entry.object_id,
                "change_message": log_entry.changes,
                "content_type": log_entry.content_type.model,
                "timestamp": log_entry.timestamp,
            }
            results.append(data)

        return Response({"results": results})
    serializer_class = LogEntrySerializer