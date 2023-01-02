from django.db import models

# Create your models here.

class Student(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    grade = models.CharField(max_length=2, blank=True, null=True)


    def __str__(self):
        return self.name
