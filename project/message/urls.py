from django.contrib import admin
from django.urls import include, path
from message import views

urlpatterns = [
    path('create/', views.create_letter, name='create_letter'),
    path('delete/<int:letter_id>/', views.delete_letter, name='delete_letter'),
    path('detail/<int:letter_id>/', views.detail_letter, name='detail_letter'),
    path('shorts_list/<int:user_id>/', views.read_letters_by_user, name='letters_by_user_id'),
]
