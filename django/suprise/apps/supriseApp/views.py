from django.shortcuts import render, redirect
import random
VALUES= ['apple', 'pop', 'bat', 'suprise', 'me', 'im', 'making', 'a', 'list', 'shorts', 'pants', 'else', 'ekse']
# Create your views here.
def index(request):
    return render(request, 'supriseApp/index.html')

def process(request):
    number= request.POST['number']
    random.shuffle(VALUES)
    print VALUES

    newlist= []
    for item in range(0, int(number)):
        newlist.append(VALUES[item])

    context={
    'VALUES': newlist,
    'number': number
    }

    return render (request, 'supriseApp/suprise.html', context)
