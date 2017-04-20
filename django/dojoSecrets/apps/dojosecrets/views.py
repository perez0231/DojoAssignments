from django.shortcuts import render
from .models import User
from django.contrib import messages
from django.db.models import Count

def index(request):

    userinsession= User.objects.get(id=request.session['user_id'])
    context= {
    "user": userinsession
    }
    return render (request, "secrets/index.html", context)

def process(request):
    if request.method == 'POST':
        return redirect("secrets/index.html")

# Create your views here.
