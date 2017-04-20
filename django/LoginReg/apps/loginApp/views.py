from django.shortcuts import render, redirect, HttpResponse
# from .models import Courses
from .models import Email
# Create your views here.
def index(request):
    return render(request, "index.html")


def process(request):
    results = Email.objects.validate(request.POST['email'])

    if results:

        context={
        'flash': results[1],
        'emails': Email.objects.all()
        }
        return render(request, 'logApp/success.html', context)


    else:

        context= {
        'false': "email not valid"
        }

        return render(request, 'index.html', context)
