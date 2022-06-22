from django.urls import path
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

from . import views
<<<<<<< HEAD
from students.views import studentReg, courseEnroll, markComplete
=======
<<<<<<< HEAD
from students.views import studentReg
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
=======
from students.views import studentReg, enroll, markComplete
>>>>>>> 76d548a5194110ce7b2ab32acc27b6c3e664be84

>>>>>>> e7329a5037782822e93898ad4fb8f582cb689023

urlpatterns = [
    path ('dashboard/', views.students, name='students'),
    path('register/', studentReg.as_view(), name='register'),
    path('login/', views.loginStudent, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('enroll/<int:pk>/',courseEnroll.as_view(), name='enroll'),
    path('complete/<int:pk>/', markComplete.as_view(), name='complete'),
    path('programs/', views.availablePrograms, name='programs'),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()