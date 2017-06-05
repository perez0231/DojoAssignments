from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.db.models import Count
from django.core.exceptions import PermissionDenied



from .models import Books, Authors, Reviews, User

# Create your views here.

def index(request):
    userinsession=User.objects.get(id=request.session['user_id'])
    context={
    "user": userinsession,
    "reviews": Reviews.objects.all().order_by('-created_at')[:3],
    "other": Reviews.objects.all().order_by('-created_at')[4:],
    }
    return render (request, "beltApp/index.html", context)


def bookreview(request):
    context={

    "author": Authors.objects.all()

    }
    return render (request, "beltApp/addreview.html", context)



def addreview(request):
    if request.method == "POST":
        book_title= request.POST['title']
        author_name= request.POST['author_input']
        if author_name =='':
            author_name=request.POST['author']


        Books.objects.create(title=book_title)

        if not Authors.objects.filter(name=author_name).exists():
            Authors.objects.create(name=author_name)


        thisbook= Books.objects.get(title= book_title)
        thisauthor=Authors.objects.get(name=author_name)
        thisauthor.books.add(thisbook)



        user_id= request.session.get('user_id')

        Reviews.objects.create(
            content= request.POST['review'],
            rating= int(request.POST['rating']),
            user= User.objects.get(id=user_id),
            books=thisbook



        )
    return redirect(reverse('beltApp:my_index'))
def bookpage(request, id):
    if request.method =="POST":
        user_id=request.session['user_id']
        reviews= Reviews.objects.create(
        content=request.POST['review'],
        rating=int(request.POST['rating']),
        user=User.objects.get(id=user_id),
        books=Books.objects.get(id=id)

        )

    data={
        'reviews': Reviews.objects.filter(books=id),
        'author': Authors.objects.get(books=id),
        "book": Books.objects.get(id=id),
        "authornames": Authors.objects.all()

        }
    return render(request, 'beltApp/bookpage.html', data)


def user(request, id):

    data={
        'user': User.objects.filter(id=id),
        'count': User.objects.filter(id=id).annotate(num_reviews=Count('Post_Review')),
        'users_reviews': Reviews.objects.filter(user=id)

    }

    return render(request, 'beltApp/user.html', data)

def delete(request, id):
    if request.user == instance.user:
        reviews.delete()
    else:
        raise PermissionDenied

    return render(request, 'beltApp/bookpage.html')



def logout(request):
    request.session.clear
    return redirect(reverse('login:my_index'))
