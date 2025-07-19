from django.db import models

# Create your models here.
class Report(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateField()
    location=models.CharField(max_length=200)
    description=models.TextField()
    severity = models.CharField(max_length=10)
    def __str__(self):
        return f"Incident reported by {self.name} on {self.date}"
from django.db import models

class Incident(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    reported_by = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    severity = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default='In Progress')

    def __str__(self):
        return self.title
