from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):

    return render(request, 'surveyApp/index.html')
def process(request):
    if request.session.get('count')== None:
        request.session['count']= 0

    if request.form == "POST":
        request.session['name']=request.POST['name']
        request.session['loc']= request.POST['location']
        request.session['language']= request.POST['lang']
        request.session['comments']= request.POST['comment']
        request.session['count'] += 1

        return  redirect('/user')
def user(request):


    return render(request, 'surveyApp/result.html')
