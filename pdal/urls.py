from django.urls import path
from django.conf.urls import url

from . import views

#from depot.views import SamplesListView, ContainerListView, LocationListView, JoinSampleContainerListView

urlpatterns = [
    #samples
    #path('samples/', views.SamplesListView, name='SamplesListView'),
    #url(r'^pdal/$', Pdal.as_view(template_name="pdal/pdal.html"), name='pdal'),
    url(r'^pdal/$', views.pdal, name='pdal'),

]
