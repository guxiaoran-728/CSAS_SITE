from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class posturl(models.Model):
    urlname = models.CharField(max_length=300)

    def __str__(self):
        return self.urlname
