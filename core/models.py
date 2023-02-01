from auditlog.registry import auditlog
from django.db import models
from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
import uuid


class School(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    max_students = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = AuditlogHistoryField()

    def __str__(self):
        return self.name

class Student(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4,editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = AuditlogHistoryField()

    def __str__(self):
        return self.student_id
    
auditlog.register(Student)