from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 100)
    course = models.CharField(max_length = 50)
    description = models.TextField()
    def __str__(self):
        return self.names

