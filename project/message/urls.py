from django.contrib import admin
from django.urls import include, path
from message import views
from message.views import LetterAPIView

urlpatterns = [
    path('create/', views.create_letter, name='create_letter'),
    path('letters/<int:user_id>/', LetterAPIView.as_view(), name='letters_by_user_id'),
]
