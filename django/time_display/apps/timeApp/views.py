from django.shortcuts import render, HttpResponse
import datetime


# Create your views here.
def index(request):
    print datetime.datetime.now()
    context={
    'currenttime': datetime.datetime.now()
    }
    return render(request, 'timeApp/index.html', context)
