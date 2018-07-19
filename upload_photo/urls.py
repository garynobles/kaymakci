from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^photos/$', views.upload, name='upload'),
]
