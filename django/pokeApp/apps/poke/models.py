from __future__ import unicode_literals

from django.db import models
import datetime
from ..login.models import User

# Create your models here.
class Poke(models.Model):
    action_user= models.ForeignKey(User, related_name="poker")
    receiver= models.ForeignKey(User, related_name="pokee")
    created_at=models.DateTimeField(auto_now_add=True)
