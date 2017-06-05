from django.shortcuts import render, redirect
from .models import User, Pokes
from django.core.urlresolvers import reverse
from django.db.models import Q, Count


# Create your views here.
def index(request):
    userinsession=User.objects.get(id=request.session['user_id'])
    curr=request.session['user_id']

    context={
    "user": userinsession,
    "allusers": User.objects.all().exclude(id=curr),
    "allpokes": Pokes.objects.all().filter(pokee=curr),
    # "userpokes": Pokes.objects.filter(pokee_id=request.session['user_id']),
    "userswhopokeme": User.objects.annotate(num_count=Count('user_poker')).filter(id=curr),
    'users':User.objects.annotate(num_count=Count('user_pokee')).exclude(id=curr),
    'mypokelist': Pokes.objects.filter(pokee= curr).values('poker').annotate(Count('poker')),
    }

    data= {
    'userinputs': len(context['mypokelist']),

    }

    context["numberofpokes"] = data['userinputs']
    print context


    # print context['userswhopokeme'][0].num_count

    return render(request, "poke/index.html", context)





def addpoke(request, id):
    if request.method=="POST":
        poker=User.objects.get(id=request.session['user_id'])
        pokee=User.objects.get(id=id)
        Pokes.objects.create(poker=poker, pokee=pokee)

    return redirect(reverse ("poke:my_index"))
def logout(request):
    request.session.clear
    return redirect(reverse('login:index'))
