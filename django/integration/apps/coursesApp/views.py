from django.shortcuts import render, redirect
from .models import Courses, User, LoginR
from django.db.models import Count
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):

    context = {
        'course_data': Courses.objects.all()

        }
    return render(request, "courses/index.html", context)


def addcourse(request):
    Courses.objects.create(name=request.POST['name'], description =request.POST['description'])
    return redirect (reverse('courses:my_index'))


def remove(request, id):
    context= {
        'course_data': Courses.objects.get(id=id)
        }
    return render(request, "courses/remove.html", context)



def nah(POST):
    return redirect('courses:my_index')


def delete(request, id):

    Courses.objects.get(id=id).delete()
    return redirect(reverse('courses:my_index'))


def choose(request):
    context = {
    'course_data': Courses.objects.all().annotate(num_users=Count ('all_courses')),
    'user': User.objects.all()

    }
    return render(request, 'courses/userReg.html', context)


def regUser(request):
    user= User.objects.get(id = request.POST['Users'])
    course = Courses.objects.get(id =request.POST['course_data'])
    login= LoginR.objects.create(user = user, course = course)
    return redirect(reverse('courses:choose'))
