from django.shortcuts import render
from .models import User
# Create your views here.
def index(request):

    return render(request, 'userApp/index.html')

def validate(request):
    userinput= User.objects.login(request.POST['username'])

    if userinput:

        context= {
        'flash': userinput[1],
        'usernames': User.objects.all()
        }
        return render(request, 'userApp/usernames.html', context)

    else:
        context= {
        'message': "email not valid"
        }

        return render (request, 'userApp/index.html', context)
