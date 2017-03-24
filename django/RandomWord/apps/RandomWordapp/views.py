from django.shortcuts import render, redirect
# Create your views here.
from django.utils.crypto import get_random_string

def index(request):

    return render(request, "RandomWord/index.html")

def WordGen(request):
    request.session['wham'] += 1 
    print request.session['wham']
    if request.method == 'POST':
        # request.session['count'] += 1
        request.session['word'] = get_random_string(length = 14)


        return redirect('/')
    else:
        return redirect('/')
