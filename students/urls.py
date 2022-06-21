from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path ('dashboard/', views.students, name='students'),
    path('login/', auth_views.LoginView.as_view(template_name='students/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)