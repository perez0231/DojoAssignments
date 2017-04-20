from django.shortcuts import render, redirect
from .models import Books
# Create your views here.
def index(request):

    context={
    'books' : Books.objects.all()

    }

    return render(request, "appBook/index.html", context)
def addbook(request):

    Books.objects.create(title=request.POST['title'], author= request.POST['author'], category= request.POST['category'])
    return redirect('/')
