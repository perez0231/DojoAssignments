from django.shortcuts import render, redirect
from .models import User, Trip, Itineraries
from django.contrib import messages
from django.core.urlresolvers import reverse
from datetime import datetime, date



# Create your views here.
def index(request):
    userinsession=request.session['user_id']
    logged=User.objects.get(id=request.session['user_id'])
    user_trips=Trip.objects.filter(traveler_id=userinsession)


    context ={
    'user': logged,
    'user_trips': Trip.objects.filter(traveler_id=userinsession),
    'trips': Trip.objects.exclude(traveler_id=userinsession)&Trip.objects.exclude(trip_planned__users_id=userinsession),
    'user_joined_trips': Itineraries.objects.filter(users=userinsession)

    }
    print context['user']
    print "*****" * 100


    return render(request, 'belt/index.html', context)


def add(request):
    return render(request,'belt/add.html')

def addinfo(request):
    if request.method=='POST':
        flag= True
        userinsession=request.session['user_id']
        data={
        'destination': request.POST['destination'],
        'description': request.POST['description'],
        'start': request.POST['start'],
        'end': request.POST['end'],
        'user_id':userinsession

        }

        process= Trip.objects.validator(data)

        if process[0]:
            return redirect(reverse('belt:my_index'))

        else:
            for item in range(len(process[1])):
                messages.error(request, process[1][item])
        return redirect(reverse('belt:add'))


    return redirect(reverse('belt:add'))



    return render (request,'belt/index.html')
def join(request, id):
    users= User.objects.get(id=request.session['user_id'])
    trips= Trip.objects.get(id=id)
    user_Itineraries= Itineraries.objects.create(users=users, trips=trips)
    return redirect(reverse('belt:my_index'))

def showtrip(request, id):
    userinsession=request.session['user_id']
    trip=Trip.objects.get(id=id)
    users=trip.traveler.id
    currTrip=Itineraries.objects.filter(trips__id=id)&Itineraries.objects.exclude(users__id=users)
    print currTrip

    context = {
    'currTrip':currTrip,
    'trip': trip,
    'user': userinsession
    }
    return render(request, 'belt/trip.html', context)



def logout(request):
    request.session.clear
    return redirect(reverse('login:my_index'))
