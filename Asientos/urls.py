from django.conf.urls import url
from django.urls import path

from Asientos import views

urlpatterns = [
     url(r'^$', views.index, name='index_Asientos'),
]