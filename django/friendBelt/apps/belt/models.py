from __future__ import unicode_literals

from django.db import models
from ..login.models import User


class Friendship(models.Model):
    user = models.ForeignKey(User, related_name="main_user")
    friend=models.ForeignKey(User,related_name="friend")
    created_at=models.DateTimeField(auto_now_add="True")

# Create your models here.
