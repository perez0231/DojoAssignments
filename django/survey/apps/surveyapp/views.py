from django.shortcuts import render, redirect
# Create your views here.
def index(request):
    return render(request, 'survey/index.html')

def process(request):
    # submit.request['name'] = session['name']
    if request.session.get("counter") == None:
        request.session["counter"] = 0

    print request.session['counter']
    if request.method == "POST":
        print request.POST['name']
        print request.POST ['location']
        print request.POST['lang']
        print request.POST['comment']

        request.session['counter'] += 1


        request.session['data']= {
        'name': request.POST['name'],
        'location': request.POST['location'],
        'language': request.POST['lang'],
        'comment': request.POST['comment']
        }
        return redirect("/results")
    else:
        return redirect("/results")
def results(request):
    print request.session['data']
    return render(request, 'survey/results.html')
