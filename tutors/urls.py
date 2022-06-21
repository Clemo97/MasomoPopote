from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

from tutors.views import TutorReg



urlpatterns = [
    path('tut/', views.tutor, name='tutor'),
    path('register-tutor/', TutorReg.as_view(), name='tutor-reg'),
    path('login-tutor/', views.loginTutor, name='tutor-login'),
    path('logout-tutor/', auth_views.LogoutView.as_view(), name='logout'),
]
