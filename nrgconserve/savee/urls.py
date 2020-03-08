from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_home, name='main_home'),
    path('', views.day_history, name='day_history'),
]