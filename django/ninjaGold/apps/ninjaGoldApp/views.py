from django.shortcuts import render, redirect
from random import randrange

def index(request):
    if 'gold' not in request.session:
        request.session['gold']= 0
    else:
        pass

    if 'message' not in request.session:
        request.session['message']= []

    return render(request, "index.html")



def process(request):
    if request.POST['building'] == 'farm':
        gold = randrange(5,10)
        print gold
        request.session['gold'] += gold
        str = "You visited farm, you earned %r gold." % (gold)
        print "here"
        request.session['message'].insert(0, str)
        print request.session['message']



    if request.POST['building'] == 'house':
        gold = randrange (1,5)
        print gold
        request.session['gold'] += gold

        str = "you visited house, you earned %r gold"% (gold)
        request.session['message'].insert(0, str)

    if request.POST['building'] == 'cave':
        gold = randrange (4, 8)
        print gold
        request.session['gold'] += gold

        str= "You went into the cave and found %r gold"%(gold)
        request.session['message'].insert(0, str)

    if request.POST['building'] == 'casino':
        gold = randrange (-50, 50)
        print gold
        request.session['gold'] += gold

        str= "You gambled and the result was %r gold"% (gold)
        request.session['message'].insert(0,str)


    return redirect("/")
# Create your views here.
