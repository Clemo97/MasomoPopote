from distutils.command.build_scripts import first_line_re
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from . models import User, Tutor, Student



class TutorRegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    contact = forms.IntegerField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        user.is_tutor = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        tutor = Tutor.objects.create(user=user)
        tutor.contact = self.cleaned_data.get('contact')
        tutor.save()
        return user


class StudentRegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        user.is_student = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save() 
        student = Student.objects.create(user=user)
        student.save()
        return user
        
    
    