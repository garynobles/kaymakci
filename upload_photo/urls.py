from django.urls import path

from . import views


urlpatterns = [
    path('photo/', views.UploadView.as_view()),
]
