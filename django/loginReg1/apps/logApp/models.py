from __future__ import unicode_literals

from django.db import models
import bcrypt
import re
EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')#CODE HERE


# Create your models here.

class UserManager(models.Manager):
    def validate(self, data): #object validatin
        flag=True
        errs = []
        if len(data['fname']) < 2 | str(data['fname']).isalpha() ==False:
            flag= False
            errs.append("cannot have less than 2 characters in first name")
        if len(data['lname']) < 2| str(data['lname']).isalpha() ==False:
            flag= False
            errs.append("cannot have less than 2 characters in last name")
        if not EMAIL_REGEX.match(data['email']): #if REGEX matches email
            flag= False
            errs.append("Must be an email@email.com format")

        if data['cpassword'] != data['password']:
            flag=False
            errs.append("Passwords do not Match")
        if len(data['password']) < 7:
            flag= False
            errs.append("Password not long enough")


        if flag:
            password=data['password']
            hashed=bcrypt.hashpw(str(password), bcrypt.gensalt())
            newuser=User.objects.create(first_name=data['fname'], last_name=data['lname'], email=data['email'], password= hashed)
            return (True, newuser)

        else:
            return (False, errs)

    def login(self, data):
        flag = True
        errs = []
        luser = User.objects.filter(email= data['email'])
        if not luser:       #if no email matach will create a QUERY SET, but if returning useer will
            flag= False
            errs.append('Invalid email')
            return (False, errs)

        if luser[0].password != data['password']:            #checking password
            flag = False
            errs.append('invalid password')
            return (False, errs)
        else:
            return (True, luser[0])



class User(models.Model):
    first_name =models.CharField(max_length=100)
    last_name =models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    objects = UserManager()
