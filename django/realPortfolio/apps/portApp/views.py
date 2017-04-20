from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render (request, 'portApp/index.html')

def project(request):
    return render (request, 'portApp/project.html')
def testimonials(request):
    return render (request, 'portApp/testimonials.html')
def about(request):
    return render (request, 'portApp/about.html')
