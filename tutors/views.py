from django.shortcuts import render


def tutor(request):
    return render(request, 'tutors/tutor.html')

