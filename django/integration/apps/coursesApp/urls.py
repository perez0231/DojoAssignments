from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name= "my_index"),
    url(r'^addcourse$', views.addcourse),
    url(r'^remove/(?P<id>\d+)$', views.remove, name= "remove"),
    url(r'^remove/nah$', views.nah),
    url(r'^delete/(?P<id>\d+)$', views.delete, name= "delete"),
    url(r'^choose$', views.choose, name ="choose"),
    url(r'^regUser$', views.regUser, name = 'regUser')

]
