from django.shortcuts import render, redirect
from .models import Courses
# Create your views here.
def index(request):
    context={
    'courses': Courses.objects.all()
    }
    return render(request, 'courses/index.html', context)
def addcourse(request):

    Courses.objects.create(name=request.POST['name'], description=request.POST['description'])

    return redirect('/')
def remove(request, id):
    context= {
    'remove': Courses.objects.filter(id=id)
    }
    return render(request, 'courses/remove.html', context)
def delete(request, id):
    context= {
    'delete': Courses.objects.filter(id=id).delete()
    }
    return redirect('/')
