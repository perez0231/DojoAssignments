from __future__ import unicode_literals

from django.db import models
from ..lrApp.models import User
# Create your models here.

class Courses(models.Model):
      name = models.CharField(max_length=200)
      description = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)

class LoginR(models.Model):
    user = models.ForeignKey(User, related_name= "all_users")
    course = models.ForeignKey(Courses, related_name= "all_courses")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
