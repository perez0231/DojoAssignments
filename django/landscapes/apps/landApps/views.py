from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'landApps/index.html')

def process(request, id):

    context = {
    'id': int(id)
    }
    return render (request, 'landApps/snow.html', context)
