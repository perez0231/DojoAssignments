from django.conf.urls import url
from . import views #from same class import views




urlpatterns = [
    url(r'^$', views.index),
    url(r'^index2$' views.index2),
]
