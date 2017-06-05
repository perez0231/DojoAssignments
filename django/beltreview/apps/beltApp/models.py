from __future__ import unicode_literals

from django.db import models
from ..logreg.models import User

# Create your models here.
class BooksManger(models.Manager):
    def validator(self, validate):
        if Books.objects.filter(title=validate['title']).exists():
            message.error(request, 'Book already is in our system')
            return True
        else:
            Books.objects.create(title=validate['title'], author=validate['author'], review=validate['review'], rating=validate['rating'])
            id=Books.objects.only('id').get(title=validate['title']).id
            return id 


class Books(models.Model):
    title= models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Authors(models.Model):
    name=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    books= models.ManyToManyField(Books, related_name= "authors")

class Reviews(models.Model):
    content= models.CharField(max_length=2000)
    rating= models.IntegerField (default = 0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user= models.ForeignKey(User, related_name="Post_Review")
    books= models.ForeignKey(Books, related_name="Book_review")
