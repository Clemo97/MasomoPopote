from multiprocessing.dummy import current_process
from threading import activeCount
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from . models import *
from . forms import *


from tutors.models import EnrolledCourse, User, Student, Course, test


def students(request):
    courses = Course.objects.all()
    tests = test.objects.all()
    currentUser = request.user.student
    activeCourses = Course.objects.filter(studentprofile=currentUser.pk).all()
    

    return render(request, 'students/dashboard.html', {'courses': courses, 'tests': tests, 'activeCourses':activeCourses})

class studentReg(CreateView):
    model = User
    form_class = StudentRegisterForm
    template_name = 'students/register.html'
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


def loginStudent(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('students')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'students/login.html',
    context={'form':AuthenticationForm()})



class enroll(LoginRequiredMixin, View):
    model = EnrolledCourse
    def post(self, request, *args, **kwargs):
        currentUser = request.user.student
        currentUser.Course.save()
        return redirect('students')

class markComplete(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        request.user.profile.enrolledIn.remove(pk=pk)
        request.user.profile.save()
        return redirect('students') 

def availablePrograms(request): 
    courses = Course.objects.all()
    return render(request, 'students/availablePrograms.html', {'courses': courses})
