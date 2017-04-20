from __future__ import unicode_literals
from django.db import models
from ..lrApp.models import User, UserManager

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class Authors(models.Model):
    name= models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add= True)
    books = models.ManyToManyField(Books, related_name= "authors")

class Review(models.Model):
    content= models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add= True)
    rating = models.IntegerField (default = 0)
    user = models.ForeignKey(User, related_name="review_post")
    book = models.ForeignKey(Books, related_name="book_reviews")    
