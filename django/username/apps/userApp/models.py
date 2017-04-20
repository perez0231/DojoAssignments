from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
      def login(self, username):
        if EMAIL_REGEX.match(username):
            username = User.objects.create(username=username)
            print username
            return(True, username)

        else:
            return False


class User(models.Model):
    username= models.CharField(max_length=45)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    objects = UserManager()



# Create your models here.
