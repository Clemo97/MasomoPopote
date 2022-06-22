from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

from tutors.views import TutorReg, addCourse,addTest



urlpatterns = [
    path('tut/', views.tutor, name='tutor'),
    path('register-tutor/', TutorReg.as_view(), name='tutor-reg'),
    path('login-tutor/', views.loginTutor, name='tutor-login'),
    path('logout-tutor/', auth_views.LogoutView.as_view(), name='logout'),
    path('new-course/', addCourse.as_view(), name='new-course'),
    path('new-test/', addTest.as_view(), name='new-test'),
]
