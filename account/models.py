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
    num=models.IntegerField(max_length=5)
    item=models.CharField(max_length=10)
    quantity=models.IntegerField(max_length=5)
    price=models.IntegerField(max_length=20)
    qxp=models.IntegerField(max_length=25)
    total=models.IntegerField(max_length=10)
    groupname_budget=models.CharField(max_length=20)
    
    
    
    def __str__(self):
        return self.item    

