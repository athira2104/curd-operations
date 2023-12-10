from django.db import models

# Create your models here. 

class Student(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField()
    roll_number = models.IntegerField()
    section = models.CharField(max_length = 3)
