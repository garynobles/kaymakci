from django.urls import path
from django.conf.urls import url

from . import views


urlpatterns = [
    # url(r'^photos/', include(namespace='gallery', app_name='gallery')),
    #url(r'^photos/$', view.gallery, name='gallery'),
    #url(r'^gallery/$', views.createphotobatch, name='createphotobatch'),
    path('', views.gallery, name='gallery'),


]
