from django.shortcuts import render, redirect
from .models import Courses
# Create your views here.
def index(request):

    context = {

        'course_data': Courses.objects.all()

        }
    return render(request, "index.html", context)


def addcourse(request):
    Courses.objects.create(name=request.POST['name'], description =request.POST['description'])

    return redirect ('/')


def remove(request, id):
    context= {
        'course_data': Courses.objects.get(id=id)
        }

    return render(request, "remove.html", context)


def nah(POST):
    return redirect('/')


def delete(requst, id):

    Courses.objects.get(id=id).delete()


    return redirect('/')
