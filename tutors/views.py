from django.shortcuts import render


def tutor(request):
    return render(request, 'tutors/tutor.html')


def register(request):
    return render(request, 'tutors/register.html')