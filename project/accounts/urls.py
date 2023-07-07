from django.urls import path, include

from accounts.views import google_callback, google_login, GoogleLogin, RegisterAPIView, AuthAPIView,get_user_email, update_nickname
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers
from .views import *
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('google/login', google_login, name='google_login'),
    path('google/callback/', google_callback, name='google_callback'),
    path('google/login/finish/', GoogleLogin.as_view(), name='google_login_todjango'),
     path('crud/nickname/', update_nickname, name='update_nickname'),
    path("register/", RegisterAPIView.as_view()),
    path("auth/", AuthAPIView.as_view()),
    path("auth/refresh/", TokenRefreshView.as_view()),
]