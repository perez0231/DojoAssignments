from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt, re

EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')#CODE HERE

# Create your views here.
def index(request):

    return render(request, "logApp/index.html")

def rprocess(request):
    data={
    'fname': request.POST['fname'],
    'lname': request.POST['lname'],
    'email': request.POST['email'],
    'password': request.POST['password'],
    'cpassword': request.POST['cpassword']

    }
    results= User.objects.validate(data)
    print results
    print "***"*100
    if results[0]:
        request.session['user_id']=results[1].id
        context={
        'success': "Sucessfully registered"
        }
        return render(request, 'logApp/success.html', context)

    else:
        for errs in results[1]:
            messages.error(request, errs)
        return redirect('/')
def login(request):
    data = {
    "email": request.POST['email'],
    "password": request.POST['password']
    }
    results = User.objects.login(data)

    if results[0]:
        request.session['user_id']= results[1].id
        return render(request, 'logApp/success.html', context)
    else:
        for err in results[1]:
            messages.error(request, err)
        return redirect ("/")

    #         return redirect("/")
