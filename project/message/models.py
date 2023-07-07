from django.db import models

from django.db import models
from accounts.models import User

# Create your models here.

class Letter(models.Model):
    #사용자 계정, 제목, 내용, 작성자, 날짜
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(default="")
    content = models.TextField()
    writer = models.TextField(default="익명")
    is_read = models.BooleanField(default=False)
    send_date = models.DateTimeField(auto_now_add=True)