from __future__ import unicode_literals

from django.db import models
from ..lrApp.models import User



# Create your models here.


class Post(models.Model):
    content = models.TextField(max_length=1000)
    creator = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(User, related_name='likes')
