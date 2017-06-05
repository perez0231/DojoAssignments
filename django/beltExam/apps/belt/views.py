from django.shortcuts import render, redirect
from .models import User, Poke
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    userinsession=User.objects.get(id=request.session['user_id'])
    print userinsession

    context={
    "user": userinsession,
    "users": User.objects.all()
    }
    return render(request, "belt/index.html", context)
def poke(request, user_id):
    action_user=User.objects.get(id=request.session['user_id'])
    receiver=request.POST['receiver_id']
    Poke.objects.create(send_user=userinsession,
                            receive_user=receive_user,
                            poke_date=time)
