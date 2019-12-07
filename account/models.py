from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, verbose_name='user',related_name='user')
    studentnum=models.CharField(max_length=10)
    groupname=models.CharField(max_length=20)
    major=models.CharField(max_length=20)
    name=models.CharField(max_length=10)

class Budget_list(models.Model):
    num=models.CharField(max_length=255)
    item=models.CharField(max_length=255)
    quantity=models.CharField(max_length=255)
    price=models.CharField(max_length=255)
    qxp=models.CharField(max_length=255)
    total=models.CharField(max_length=255)
    groupname_budget=models.CharField(max_length=255)
    people=models.CharField(max_length=255, default=0)
    state=models.IntegerField(default=0)
    
    def __str__(self):
        return self.groupname_budget 

