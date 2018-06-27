from django.urls import path
from django.conf.urls import url

from . import views
#qnisp
url(r'^qnisp/$', views.allqnisp, name='allqnisp'),
