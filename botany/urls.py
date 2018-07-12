from django.urls import path

from . import views

urlpatterns = [
    path('', views.allbotany, name='allbotany'),
    #path('<int:blog_id>/', views.detail, name='detail'),


    path('', views.allfraction, name='allfraction'),


]
