from django.shortcuts import render, HttpResponse

#controler

def index(request):
    print ("*" * 100)
    return render(request, "templates/first_app/index.html")
# Create your views here.
