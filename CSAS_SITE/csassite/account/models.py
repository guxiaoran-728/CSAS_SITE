from django.db import models

# Create your models here.


class User(models.Model):          # 创建用户类
    username = models.CharField(max_length=20)
    userpassword = models.CharField(max_length=20)
    userob = models.Manager()

