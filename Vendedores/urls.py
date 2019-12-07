from django.conf.urls import url
from django.urls import path

from Vendedores import views

urlpatterns = [
     url(r'^$', views.index, name='index_Vendedores'),
]