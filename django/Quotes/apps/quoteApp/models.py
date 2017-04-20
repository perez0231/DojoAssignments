from __future__ import unicode_literals
from django.db import models
from ..lrApp.models import User, UserManager
# Create your models here.


class Quotes(models.Model):
    content= models.CharField(max_length = 1000)
    author= models.CharField(max_length= 1000)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="subpost")


class Favorite(models.Model)
    user = models.ForeignKey(User, related_name="like")
