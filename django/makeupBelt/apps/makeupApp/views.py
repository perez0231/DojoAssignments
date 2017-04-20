from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from ..logReg.models import User
# Create your views here.
def index(request):
    if request.session['user_id'] == None:
		return redirect('/')
    user = User.objects.get(alias=request.session['id'])
    users= User,




    userinsession= User.objects.get(id=request.session['user_id'])

    # exclude = User.objects.all().exclude(Friend1 = User.objects.filter(request.session['user_id']))
    context= {
    "user": userinsession,
    # "users": User.objects.exclude(id = request.session['user_id'])&User.objects.exclude(friend1 = ),
    "users":  User.objects.exclude(id = request.session['user_id']),
    "friendships":Friend.objects.filter(Friend1 = request.session['user_id'])
    }

    return render (request, "makeup/index.html", context)

def add(request, id):
    if request.method =="POST":

        friend_1= User.objects.get(id=request.session['user_id'])
        friend_2= User.objects.get(id=id)
        friendship = Friend.objects.create(Friend1= friend_1, Friend2=friend_2)
        return redirect (reverse("makeupApp:index"))
