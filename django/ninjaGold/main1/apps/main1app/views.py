from django.shortcuts import render
from .models import People
# Create your views here.
def index(request):
    People.objects.create(first_name="mike", last_name="guy")
    people = People.objects.all()
    print (people)
    return render (request, "index.html")
