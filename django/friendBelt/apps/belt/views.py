from django.shortcuts import render, redirect
from .models import User, Friendship
from django.core.urlresolvers import reverse


# Create your views here.
def index(request):
    logged=User.objects.get(id=request.session['user_id'])
    user_id =request.session['user_id']

    not_friends_yet = []
    already_friends = {}
    already_friends_list = []

    all_friendships = Friendship.objects.all()



    friendships_im_in = Friendship.objects.filter(user = user_id)
    all_users = User.objects.all().exclude(id = user_id)

    for friend_object in friendships_im_in:
        already_friends[friend_object.friend.id] = friend_object.friend
        already_friends_list.append(friend_object.friend)


    print ("already friend list", already_friends_list)

    for user in all_users:
        if user.id not in already_friends:
            not_friends_yet.append(user)

    print not_friends_yet

    context={
    'user': logged,
    'not_friends_yet': not_friends_yet,
    'already_friends': already_friends_list
    }

    # print context['all_friends']
    return render(request, "belt/index.html", context)


def addfriend(request, id):
    if request.method == "POST":
        user=  User.objects.get(id=request.session['user_id'])
        friend= User.objects.get(id=id)
        Friendship.objects.create(user=user, friend=friend)

    return redirect(reverse('belt:my_index'))

def logout(request):
    request.session.clear
    return redirect(reverse('login:my_index'))
