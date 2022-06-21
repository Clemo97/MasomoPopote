from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_tutor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email=models.EmailField()

class Tutor(models.Model):
    user = models.OneToOneField(User, related_name='tutor', on_delete = models.CASCADE, primary_key = True)
    # contact = models.IntegerField()

# class CourseCategory(models.Model):
#     title=models.CharField(max_length=100)
#     descriptions=models.TextField()

class Course(models.Model):
    tutor=models.ForeignKey(Tutor, on_delete=models.CASCADE)
    title=models.CharField(max_length=100) 
    descriptions=models.TextField()
    body = models.TextField()
    course_poster = models.ImageField(upload_to='coursePoster')
    category = models.CharField(max_length=100)



class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True) 
    courseInterest = models.TextField() 

class test(models.Model):
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()

