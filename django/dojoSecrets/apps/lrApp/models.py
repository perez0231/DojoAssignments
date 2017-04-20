from __future__ import unicode_literals
from django.db import models
import bcrypt, re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')#CODE HERE

class UserManager(models.Manager):
    def validator(self, data):#self-function, object of function
        flag = True
        errs = []
        if len(data['fname']) < 2:
            flag= False
            errs.append("Cannot have less than 2 characters in First Name")

        if len(data['lname']) < 2:
            flag = False
            errs.append("Cannot have less than 2 characters in Last Name")

        if data['password'] != data['cpassword']:
            flag= False
            errs.append("Passwords do not Match")



        if flag: # if true, this data is returned to the DB, returns user object

            user= User.objects.create(fname= data['fname'],lname=data['lname'], email= data['email'], password= data['password'])

            return (True, user)
        else: ### else if not true return False spit out errs report
            return(False, errs)

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
    fname = models.CharField(max_length=35)
    lname = models.CharField(max_length=35)
    email = models.EmailField(max_length=55)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
