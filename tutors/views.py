from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView
from django.views.generic import DeleteView, ListView, UpdateView,DetailView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


from .models import *
from .forms import *


def tutor(request):
    return render(request, 'tutors/tutor.html')


# def register(request):

#     return render(request, 'tutors/register.html')



class TutorReg(CreateView):
    model = User
    form_class = TutorRegisterForm
    template_name = 'tutors/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('tutor-login')


def loginTutor(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('tutor')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'tutors/login.html',
    context={'form':AuthenticationForm()})



class addCourse(LoginRequiredMixin, CreateView):
    model = Course
    fields = ['title', 'descriptions', 'body','category','course_poster']
    template_name = 'tutors/newCourse.html'
    def form_valid(self, form):
        form.instance.tutor=self.request.user
        return super().form_valid(form)

class addTest(LoginRequiredMixin, CreateView):
    model = test
    fields = ['title', 'body','course']
    template_name = 'tutors/newTest.html'
    def form_valid(self, form):
        # form.instance.tutor=self.request.user
        return super().form_valid(form)
