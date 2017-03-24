from django.shortcuts import render, redirect


def index(request):
    return render(request, "index.html")

def ninjas(request):
    context = {
    'display': True
    }
    return render(request, "ninjatwo.html", context)

def colors(request, color):
    context = {
    'display': False,
    'color': color
    }

    return render(request, "ninjatwo.html", context)

# Create your views here.
