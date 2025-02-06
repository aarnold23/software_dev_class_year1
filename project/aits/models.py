

# Create your models here.
from django.db import models


class User(models.Model):
   firstname = models.CharField(max_length=200)
   lastname = models.CharField(max_length=200)
   student_number = models.IntegerField(default=0)
   

class Issues(models.Model):
   issues = models.CharField(max_length=200)
   pub_date = models.DateTimeField("date published")
   user = models.ForeignKey(User, on_delete=models.CASCADE)

class Department(models.Model):
   name = models.CharField(max_length=200)
