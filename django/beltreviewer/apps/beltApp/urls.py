from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bookreview$', views.bookreview, name="bookreview"),
    url(r'^add$', views.add, name="add"),
    url(r'^bookpage/(?P<id>\d+)$', views.bookpage, name = "bookpage"),
    url(r'^addtoreview/(?P<id>\d+)$', views.addtoreview, name = "addtoreview"),
    url(r'^userpage/(?P<id>\d+)$', views.userpage, name = "userpage")

]
