from django.urls import path, include

from accounts.views import google_callback, google_login, GoogleLogin, RegisterAPIView, AuthAPIView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register('list', UserViewSet)

urlpatterns = [
    path('google/login', google_login, name='google_login'),
    path('google/callback/', google_callback, name='google_callback'),
    path('google/login/finish/', GoogleLogin.as_view(), name='google_login_todjango'),
    path("register/", RegisterAPIView.as_view()),
    path("auth/", AuthAPIView.as_view()),
    path("auth/refresh/", TokenRefreshView.as_view()),
    path("", include(router.urls)),
]