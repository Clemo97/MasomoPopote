from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from PIL import Image


class User(AbstractUser):
    is_tutor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email=models.EmailField()


class Tutor(models.Model):
    user = models.OneToOneField(User, related_name='tutor', on_delete = models.CASCADE, primary_key = True)
    def __str__(self):
            return self.user.first_name


class Course(models.Model):
    tutor=models.ForeignKey(Tutor, on_delete=models.CASCADE)
    title=models.CharField(max_length=100) 
    descriptions=models.TextField()
    body = models.TextField()
    coursePoster = models.ImageField(upload_to='coursePoster')
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
            return reverse('tutor')



class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='student',primary_key = True) 
    # courseInterest = models.TextField()

    def __str__(self):
        return self.user.first_name


class StudentProfile(models.Model):
    user = models.ForeignKey(Student, on_delete = models.CASCADE)
    profileImage = models.ImageField(default='default.png',upload_to='profilePics')
    enrolledIn = models.ForeignKey(Course, on_delete = models.CASCADE,  null=True)
    

    def __str__(self):
        return f'{self.user}profile'


class EnrolledCourse(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE, null=True, related_name='enrolledStudent')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, related_name='courseEnroll')

    def get_absolute_url(self):
            return reverse('dashboard')
            

class test(models.Model):
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
            return reverse('tutor')

