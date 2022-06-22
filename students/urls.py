from django.urls import path
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

from . import views
from students.views import studentReg
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path ('dashboard/', views.students, name='students'),
    path('register/', studentReg.as_view(), name='register'),
    path('login/', views.loginStudent, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()