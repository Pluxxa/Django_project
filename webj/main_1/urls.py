# main_1/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new, name='new'),
]
