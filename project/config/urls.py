from django.contrib import admin
from django.urls import include, path
from message import views

app_name = 'letters'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('letters/<int:letter_id>/', views.read_letter_detail, name='read_letter_detail'),
    path('letters/<int:letter_id>/delete/', views.delete_letter, name='delete_letter'),
    path('letters/create/', views.create_letter, name='create_letter'),
]