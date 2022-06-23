from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from . import views
from django.conf.urls.static import static

from tutors.views import TutorReg, addCourse,addTest
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('tut/', views.tutor, name='tutor'),
    path('register-tutor/', TutorReg.as_view(), name='tutor-reg'),
    path('login-tutor/', views.loginTutor, name='tutor-login'),
    path('logout-tutor/', auth_views.LogoutView.as_view(), name='tutor-logout'),
    path('new-course/', addCourse.as_view(), name='new-course'),
    path('new-test/', addTest.as_view(), name='new-test'),
    path('posted-tests/', views.publishedTests, name = 'postedTest'), #postedTests
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
