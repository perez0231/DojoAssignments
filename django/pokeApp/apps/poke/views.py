# Create your views here.
from django.shortcuts import render, redirect
from .models import User, Poke
from django.core.urlresolvers import reverse
from django.db.models import Q, Count


# Create your views here.
def index(request):
    logged=User.objects.get(id=request.session['user_id'])
    user=request.session['user_id']
    users_pokes= Poke.objects.filter(receiver_id=request.session['user_id'])
    alluserpoke=Poke.objects.filter(receiver=logged).order_by('action_user_id')
    poking_set=set()
    indivpokers= []
    for item in alluserpoke:
        if item.action_user_id not in poking_set:
            indivpokers.append(item)
            poking_set.add(item.action_user_id)
        mytotalpokes=len(indivpokers)



    context={
    "mypokes": mytotalpokes,
    "user": logged,
    "allusers": User.objects.all().exclude(id=user),
    'poke_list': Poke.objects.all().filter(receiver_id=user),
    'users': User.objects.annotate(num_count=Count('pokee')).exclude(id=user),
    'userpokes': Poke.objects.filter(receiver_id=request.session['user_id']).values('action_user').annotate(Count('action_user'))
    }

    return render(request, "poke/index.html", context)
def addpoke(request, id):
    if request.method == "POST":
        sender=  User.objects.get(id=request.session['user_id'])
        user= User.objects.get(id=id)
        Poke.objects.create(action_user=sender, receiver=user)

    return redirect(reverse('poke:my_index'))


def logout(request):
    request.session.clear
    return redirect(reverse('login:my_index'))
