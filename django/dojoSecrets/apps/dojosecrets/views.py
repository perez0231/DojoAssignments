from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from ..lrApp.models import User
from .models import Post
from django.contrib import messages
from django.db.models import Count

def index(request):

    userinsession= User.objects.get(id=request.session['user_id'])

    context= {
    "user": userinsession,
    "secrets": Post.objects.all().order_by('-created_at').filter()[:5],

    }
    return render (request, "secrets/index.html", context)

def process(request):
    if request.method == 'POST':
        user=User.objects.get(id=request.session['user_id'])

        Post.objects.create(content=request.POST['secret'], creator=user)
        return redirect(reverse("dojosecrets:my_index"))

# Create your views here.
