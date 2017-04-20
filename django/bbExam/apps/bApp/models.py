from __future__ import unicode_literals
from django.db import models
from ..lrApp.models import User, UserManager


# Create your models here.
class Friends(models.Model):
    friend = models.ManyToManyField(User, related_name="friendship")
    created_at = models.DateTimeField(auto_now_add= True)
