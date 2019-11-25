from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, verbose_name='user',related_name='user')
    studentnum=models.CharField(max_length=10)
    groupname=models.CharField(max_length=20)
    major=models.CharField(max_length=20)
    name=models.CharField(max_length=10)
    