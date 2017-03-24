from __future__ import unicode_literals

from django.db import models

import re #import regex

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')#CODE HERE
# Create your models here.
class EmailManager(models.Manager): #import classmanager
    def validate(self, email): #object validating
        if EMAIL_REGEX.match(email): #if REGEX matches email
            email=Email.objects.create(email=email) #create variable email
            print email
            return (True, email) #return true flag, and email var above
        else:
            return False # false flag



class Email(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)


    objects = EmailManager()
