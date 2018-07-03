from django.urls import path
from django.conf.urls import url

from . import views

from spatial3d.views import PhotobatchListView

urlpatterns = [
    #photobatch

    #url(r'^""$', PhotobatchListView.as_view(template_name="photobatch/allphotobatch.html"), name='allphotobatch'),
    path('photobatch/', PhotobatchListView.as_view(template_name="photobatch/allphotobatch.html"), name='allphotobatch'),


    path('photobatch/<int:sample_id>/', views.detailphotobatch, name='detailphotobatch'),
    url(r'^photobatch/edit/(?P<pk>\d+)/edit/$', views.editphotobatch, name='editphotobatch'),
    url(r'^photobatch/createphotobatch/$', views.createphotobatch, name='createphotobatch'),


]
