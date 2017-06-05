from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="my_index"),
    url(r'^/addfriend/(?P<id>\d+)$', views.addfriend, name="addfriend"),
    url(r'^logout$', views.logout, name="logout"),

    ]
