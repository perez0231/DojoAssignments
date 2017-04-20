
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import User
# Create your views here.
def index(request):
    if request.session['user_id'] == None:
		return redirect('/')

    userinsession= User.objects.get(alias=request.session['user_id'])


    context= {
    "user": userinsession,
    "user": User.objects.all
    }

    return render (request, "examApp/index.html", context)
