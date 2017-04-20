from __future__ import unicode_literals
from django.db import models
from ..logReg.models import User, UserManager
# Create your models here.
class Friend(models.Model):
    Friend1 = models.ForeignKey(User, related_name = "friend1")
    Friend2 = models.ForeignKey(User, related_name = "friend2")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
