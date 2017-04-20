from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name= "index"),
    url(r'^addquote$', views.addquote, name= "addquote"),
    url(r'^makefav/(?P<id>\d+)$', views.makefav, name="makefav"),
    url(r'^user/(?P<id>\d+)$', views.user, name="user"),
    url(r'^remove/(?P<id>\d+)$', views.remove, name="remove"),
    url(r'^dashboard$', views.dashboard, name= "dashboard"),



]
