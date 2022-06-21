from cmath import log
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView
from .models import *
from .forms import *


def tutor(request):
    return render(request, 'tutors/tutor.html')


def register(request):

    return render(request, 'tutors/register.html')

class studentReg(CreateView):
    model = User
    form_class = StudentRegisterForm
    template_name = 'tutors/student.html'
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('student')

class TutorReg(CreateView):
    model = User
    form_class = TutorRegisterForm
    template_name = 'tutors/registration.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('tutor')