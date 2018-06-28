from django.urls import path
from django.conf.urls import url

from . import views


urlpatterns = [
    #url(r'^$', CurrencyListView.as_view()),
    url(r'^test_pagefilter/test_filter/$', CurrencyListView.as_view(template_name="currency_filter.html")),
    #url(r'^createstore/$', views.createstore, name='createstore'),
]
