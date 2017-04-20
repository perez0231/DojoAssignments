from django.shortcuts import render, redirect
from random import randrange

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold']= 0
    else:
        pass

    if 'userslog' not in request.session:
        request.session['userslog']= []
    return render(request, "index.html")


def process(request):
    if request.POST['building'] == 'farm':
        randnum= randrange(10, 20)
        request.session['gold'] += randnum
        str="You earned {} from the farm".format(randnum)
        request.session['userslog'].insert(0, msg)

    if request.POST['building'] == 'cave':
        randnum= randrange(5, 10)
        request.session['gold'] += randnum
        str="You earned {} from the cave".format(randnum)
        request.session['userslog'].insert(0, str)
    if request.POST['building'] == 'house':
        randnum= randrange(2, 5)
        request.session['gold'] += randnum
        str="You earned {} from the house".format(randnum)
        request.session['userslog'].insert(0, str)


    if request.POST['building'] == 'casino':
        randnum= randrange(-50, 50)
        request.session['gold'] += randnum
        str="You earned {} from the casino".format(randnum)
        request.session['userslog'].insert(0, str)
    return redirect('/')
