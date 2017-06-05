from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='my_index'),
    url(r'^addpoke/(?P<id>\d+)$', views.addpoke, name='addpoke'),
    url(r'^logout$', views.logout, name='logout'),

    ]
