from __future__ import unicode_literals

from django.db import models

# Create your models here
class Products(models.Model):
    name= models.CharField(max_length=100)
    description= models.CharField(max_length=100)
    weight= models.IntegerField()
    cost= models.IntegerField()
    category= models.CharField(max_length=100)
