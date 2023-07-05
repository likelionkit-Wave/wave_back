from django.contrib import admin
from django.urls import include, path
from message import views

urlpatterns = [
    path('create/', views.create_letter, name='create_letter'),
]
