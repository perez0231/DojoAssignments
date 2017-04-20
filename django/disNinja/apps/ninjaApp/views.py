from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, "ninjaApp/index.html")
def ninjas(request):
    context={
    'display': True
    }
    return render(request,'ninjaApp/ninjas.html', context)

def indiv(request, color):
    context={
    'display': False,
    'color': color
    }
    return render(request, "ninjaApp/ninjas.html", context)
