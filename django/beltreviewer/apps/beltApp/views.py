from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from .models import Books, Authors, Review, User
# Create your views here.
def index(request):
    userinsession= User.objects.get(id=request.session['user_id'])



    context= {
    "user": userinsession,
    "review": Review.objects.all().order_by('-created_at')[:3],
    "other_review": Review.objects.all().order_by('-created_at')[3:]
    }


    return render (request, "libary/index.html", context)



def bookreview(request): #add
    data = {
    "authors" : Authors.objects.all()
    }


    return render (request, "libary/bookreview.html", data)

def add(request): #review

    if request.method == "POST":
        book_title = request.POST['title']
        author_name=request.POST['author_input']
        if author_name == '':
            author_name= request.POST['selectAuthor']

        Books.objects.create(
            title = book_title
        )

        if not Authors.objects.filter(name=author_name).exists():
            Authors.objects.create(name=author_name)

        this_book = Books.objects.get(title=book_title)
        this_author= Authors.objects.get(name = author_name)
        this_author.books.add(this_book)

        user = request.session.get('user_id')

        Review.objects.create(
            content = request.POST['review'],
            rating = int(request.POST['rating']),
            user = User.objects.get(id=user),
            book= this_book
        )



    return redirect(reverse('beltApp:index'))

def bookpage(request, id):
    # if request.method =="POST":
        # reviews=  Review.objects.create(
        #     content = request.POST['review'],
        #     rating= int(request.POST['rating']),
        #     book= Books.objects.get(id=id)
        # )
        data = {
        "book" : Books.objects.get(id=id),
        "author" : Authors.objects.get(books__id=id),
        "reviews" : Review.objects.filter(book__id=id)
    }

        return render(request, 'libary/bookpage.html', data)

def addtoreview(request, id):
    if request.method == "POST":

    	    reviews = Review.objects.create(
    		content = request.POST['rev'],
    		rating = int(request.POST['rating']),
    		user = User.objects.get(id= request.session['user_id']),
    		book = Books.objects.get(id=id)
            )

    data = {'reviews': Review.objects.filter(book=id),
        'book': Books.objects.get(id=id),
        'author': Authors.objects.get(books=id)
        	}
    return render(request, 'libary/bookpage.html', data)


def userpage(request, id):
    data = {
    'user': User.objects.filter(id=id).annotate(num_reviews=Count('review_post')),
    'userreviews': Reviews.objects.filter(user= id)

    }



    return render(request, 'libary/userpage.html', data)
