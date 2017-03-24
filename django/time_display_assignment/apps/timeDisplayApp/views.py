from django.shortcuts import render, redirect
# Create your views here.
import datetime

def index(request):
    print datetime.datetime.now()
    context = {
    'currenttime': datetime.datetime.now()

    }

    print request.session
    request.session['currtime']= datetime.datetime.now().strftime('%H: %M')
    print request.session['currTime']

    return render(request, "index.html", context)

def index2 (request):
    print request.session['currTime']
    return redirect("/")
