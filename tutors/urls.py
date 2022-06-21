from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

from views import TutorReg



urlpatterns = [
    path('tut/', views.tutor, name='tutor'),
    path('regiser-tutor', TutorReg.as_view(), name='tutor-reg')
     path('login/', auth_views.LoginView.as_view(template_name='tutors/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
