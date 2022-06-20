from django.urls import path
from . import views



urlpatterns = [
    path('tut', views.tutor, name='tutor'),
]
