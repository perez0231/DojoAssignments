from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add$', views.add, name="add"),
    url(r'^users$', views.users, name="users"),
    url(r'^int/(?P<id>\d+)$', views.int, name="int")
]
