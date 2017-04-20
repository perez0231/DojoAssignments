from __future__ import unicode_literals
from django.db import models
from ..lrApp.models import User, UserManager

# Create your models here.
class Friends(models.Model):
    friendship = models.ForeignKey(User, related_name = "friend1")
    frienship2 = models.ForeignKey(User, related_name = "friend2")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
