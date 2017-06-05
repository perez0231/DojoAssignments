from __future__ import unicode_literals

from django.db import models
import datetime
from ..login.models import User





# Create your models here.
class Pokes(models.Model):
    poker=models.ForeignKey(User, related_name="user_poker")
    pokee=models.ForeignKey(User, related_name="user_pokee")
    created_at=models.DateTimeField(auto_now_add=True)
    
