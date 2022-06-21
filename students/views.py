from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import login, logout, authenticate


from . models import *
from . forms import *

def students(request):

    return render(request, 'students/dashboard.html')

class studentReg(CreateView):
    model = User
    form_class = StudentRegisterForm
    template_name = 'tutors/student.html'
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('student')