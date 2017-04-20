from __future__ import unicode_literals
from django.db import models
from ..lrApp.models import User, UserManager
# Create your models here.

class QuotesManager(models.Manager):
    def validator(self, data):
        flag = False
        errs= []
        if len(data['author']) < 3:
            flag = True
            errs.append("Cannot have less than 2 characters in Quoted by")
        if len(data['content']) < 10:
            flag = True
            errs.append("Cannot have less than 10 characters in Quote")

        if flag:
            post= Quotes.objects.create(content= request.POST['quote'], author=request.POST['quoted'], user= request.session['user_id'])

            return (True, post)

        else:
            return(False, errs)

class Quotes(models.Model):
    content= models.CharField(max_length = 1000)
    author= models.CharField(max_length= 1000)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="subpost")
    objects = QuotesManager()


class Favorite(models.Model):
    user = models.ForeignKey(User, related_name="like")
    quote = models.ForeignKey(Quotes, related_name= "fav_quote")
    created_at= models.DateTimeField(auto_now_add=True)
