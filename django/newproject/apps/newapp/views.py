from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    print "here"
    return render(request,'index.html')
