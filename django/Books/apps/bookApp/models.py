from __future__ import unicode_literals

from django.db import models

# Create your models here.
class books(models.Model):
    title= models.CharField(max_length=100)
    author= models.CharField(max_length=100)
    publishedDate= models.DateTimeField()
    category= title= models.CharField(max_length=100)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
