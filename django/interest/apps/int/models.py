from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    name=models.CharField(max_length=40)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

class Interests(models.Model):
    interest=models.TextField(max_length=4000)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

class UsersInterests(models.Model):
    user= models.ForeignKey(User, related_name="mainuser")
    interest= models.ForeignKey(Interests, related_name="maininterest")


# Create your models here.
