from __future__ import unicode_literals
import re
from datetime import date, datetime
from django.db import models
from ..login.models import User


class TripManager(models.Manager):
    def validator(self, data):
        messages= []
        flag =False

        if not data['destination'] or not data['description'] or not data['start'] or not data['end']:
            flag = True
            messages.append('no fields can be blank')

        if not data['start'] or not data['end']:
            flag = True
            messages.append('You must enter a start and end date')
        else:
            if data['start']:
                startdate= datetime.strptime(data['start'], '%Y-%m-%d')
            if data['end']:
                enddate = datetime.strptime(data['end'], '%Y-%m-%d')

            if startdate < datetime.now():
                flag = True
                messages.append('All trips must start on a future date, not in the past')

            if startdate > enddate:
                flag = True
                messages.append('Travel end date cannot be before start date')

        if not flag:
            print data['user_id']
            trip = Trip.objects.create(destination=data['destination'],
            plan=data['description'], startdate=data['start'], enddate=data['end'], traveler_id=data['user_id'])
            print data['user_id']
            print "*" * 100
            return (True, trip)

        else:
            return(False, messages)






# Create your models here.
class Trip(models.Model):
    destination=models.CharField(max_length=100)
    startdate=models.DateTimeField()
    enddate=models.DateTimeField()
    plan=models.CharField(max_length=1000)
    created_at=models.DateTimeField(auto_now_add=True)
    traveler=models.ForeignKey(User, related_name="trip_users")
    objects = TripManager()
class Itineraries(models.Model):
    users= models.ForeignKey(User, related_name="going_user")
    trips=models.ForeignKey(Trip, related_name="trip_planned")
