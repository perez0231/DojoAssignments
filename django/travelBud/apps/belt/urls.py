from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="my_index"),
    url(r'^add$', views.add, name="add"),
    url(r'^addinfo$', views.addinfo, name="addinfo"),
    url(r'^join/(?P<id>\d+)$', views.join, name="join"),
    url(r'^showtrip/(?P<id>\d+)$', views.showtrip, name="showtrip"),
    url(r'^logout$', views.logout, name='logout'),


    ]
