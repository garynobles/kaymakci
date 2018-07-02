from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
#qnisp
    url(r'^qnisp/$', views.allqnisp, name='allqnisp'),
    url(r'^qnisp/createqnisp/$', views.createqnisp, name='createqnisp'),
    url(r'^qnisp/edit/(?P<pk>\d+)/edit/$', views.editqnisp, name='editqnisp'),
    #url(r'^qnisp/search/edit/(?P<pk>\d+)/edit/$', views.editqnispsearch, name='editqnispsearch'),
]
