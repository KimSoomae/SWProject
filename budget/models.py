from django.db import models

# Create your models here.

class Budget_list(models.Model):
    num=models.IntegerField(max_length=5)
    item=models.CharField(max_length=10)
    quantity=models.IntegerField(max_length=5)
    price=models.IntegerField(max_length=20)
    qxp=models.IntegerField(max_length=25)
    check=models.CharField(max_length=2)
    status=models.CharField(max_length=5)
    
    def __str__(self):
        return self.item

    
