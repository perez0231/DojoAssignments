from django.conf.urls import url
from . import views           # This line is new!

#Models views templates


def index(request):
    print ("banana")

urlpatterns =[
    url(r'^$', views.index)     # This line has changed!
    
  ]
