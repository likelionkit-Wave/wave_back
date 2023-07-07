
from django.contrib import admin
from django.urls import include, path
from message import views
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('allauth.urls')),
    path('api/accounts/', include('accounts.urls')),
    path('api/message/', include('message.urls')),
]
