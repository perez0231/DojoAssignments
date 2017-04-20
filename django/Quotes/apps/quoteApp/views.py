from django.shortcuts import render
from django.core.urlresolvers import reverse
from .models import User, Quotes


# Create your views here.

def index(request):
    userinsession= User.objects.get(id=request.session['user_id'])

    context= {
    "user": userinsession,

    }
    return render(request, 'quoteApp/index.html', context)


def addquote(request):
    if request.method == "POST":

        Quotes.objects.create(
        content=request.POST['quote'],
        author=request.POST['quoted']
        )

    return render(request, 'quoteApp/index.html')
