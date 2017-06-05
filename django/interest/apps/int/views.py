from django.shortcuts import render, redirect
from .models import User, Interests, UsersInterests
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    return render(request, 'int/index.html')

def add(request):
    if request.method == "POST":
        if User.objects.filter(name=request.POST['name']):
            user = User.objects.get(name=request.POST['name'])
        else:
            user = User.objects.create(name = request.POST['name'])
        if Interests.objects.filter(interest=request.POST['interest']):
            interest = Interests.objects.get(interest=request.POST['interest'])
        else:
            interest = Interests.objects.create(interest = request.POST['interest'])
            print "here are the interests"
        UsersInterests.objects.create(user=user, interest=interest)
    return redirect(reverse('int:users'))


def users(request):
    context={
    'Users': User.objects.all()
    }
    print context['Users'][0]
    return render(request, 'int/show.html', context)

def int(request, id):
    context={
    'interests': UsersInterests.objects.filter(user__id=id)
    }
    return render(request, 'int/interest.html', context)
