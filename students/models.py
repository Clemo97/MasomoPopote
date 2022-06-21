from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_tutor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email=models.EmailField()

    

class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True) 
    courseInterest = models.TextField() 
