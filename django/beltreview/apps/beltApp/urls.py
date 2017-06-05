from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='my_index'),
    url(r'^bookreview$', views.bookreview, name='bookreview'),
    url(r'^addreview$', views.addreview, name='addreview'),
    url(r'^bookpage/(?P<id>\d+)$', views.bookpage, name='bookpage'),
    url(r'^user/(?P<id>\d+)$', views.user, name='user'),
    url(r'^logout$', views.logout, name='logout'),




]
