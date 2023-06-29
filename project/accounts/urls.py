from django.urls import path
from accounts.views import UserCreateAPIView, CustomAuthToken

urlpatterns = [
    path('api/register/', UserCreateAPIView.as_view(), name='user-register'),
    path('api/login/', CustomAuthToken.as_view(), name='login'),
]