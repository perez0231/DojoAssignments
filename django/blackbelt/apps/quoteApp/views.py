from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import User, UserManager, Quotes, Favorite
from django.db.models import Count
from django.contrib import messages


from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import User
import bcrypt, re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
	return render(request, 'loginReg/index.html')

def validate(request):

	data = {
		"name" : request.POST['name'],
		"alias" : request.POST['user_name'],
		"password" : request.POST['password'],
		"passconfirm" : request.POST['passconfirm']
	}

	result = User.objects.validate(data)

	if result[0]:
		request.session['user_id'] = result[1].id
		context = {
		'success': "You have Succesfully Registered! Thank you!"
		}
		return render(request, 'loginReg/index.html', context)
	else:
		for err in result[1]:
			messages.error(request, err)
		return redirect('/')

def success(request):
	if request.method == 'POST':
		username = request.POST['user_name']
		password = request.POST['password']
		if not User.objects.filter(username=username):
			context = {
				'error': 'Username Not Found'
			}
			return render(request, 'loginReg/index.html', context)
		user = User.objects.filter(username=username)
		if bcrypt.hashpw(str(password), str(user[0].password)) == user[0].password:
			request.session['user'] = user[0].id
		else:
			context = {
			'pass': "Password Not Valid"
			}
			return render(request, 'loginReg/index.html', context)

		return redirect(reverse('black:my_index'))

def logout(request):
	request.session.clear()
	return redirect('/')

# Create your views here.

def index(request):
    userinsession= User.objects.get(id=request.session['user_id'])


    context= {
    "user": userinsession,
    "quotes": Quotes.objects.all().exclude(fav_quote__user = userinsession),
    "favs": Favorite.objects.all().filter(user= userinsession)[:3]
    }

    return render (request, "quoteApp/index.html", context)



def addquote(request):
    if request.method == "POST":
        user= request.session['user_id']

        data= {
        "content":request.POST['quote'],
        "author":request.POST['quoted']
        }

        results = Quotes.objects.validator(data)

        if results[0]:

            return redirect(reverse('quoteApp:index'))
        else:
            for err in results[1]:
                messages.error(request, err)
            return redirect(reverse('quoteApp:index'))


    return redirect(reverse('quoteApp:index'))

def makefav(request, id):
    if request.method == "POST":
        user= User.objects.get(id= request.session['user_id'])
        quotes =Quotes.objects.get (id=id)
        Favorite.objects.create(user=user, quote= quotes)

    return redirect(reverse('quoteApp:index'))

def user(request, id):
    user=User.objects.get(id= id)

    context= {
    "user": user,
    "quotes": Quotes.objects.all().filter(user = user),
    "count" : User.objects.filter(id= id).annotate(poop= Count('subpost'))
    }
    return render (request, "quoteApp/user.html", context)


def remove(request, id):
    if request.method == "POST":
        Favorite.objects.get(id=id).delete()
        print id


    return redirect(reverse('quoteApp:index'))



def dashboard(request):
    return redirect(reverse('quoteApp:index'))
