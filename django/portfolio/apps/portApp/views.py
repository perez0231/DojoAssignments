from django.shortcuts import render

# Create your views here.
def index(request):
    print "here"
    return render(request, 'portApp/index.html')
def testimonials(request):
    print "here"
    return render(request, 'portApp/testimonials.html')
