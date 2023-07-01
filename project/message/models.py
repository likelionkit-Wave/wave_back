from django.db import models

from django.db import models
from accounts.models import User

# Create your models here.

class Letter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    send_date = models.DateTimeField(auto_now_add=True)