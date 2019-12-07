from django.conf.urls import url

from Clientes import views

urlpatterns = [
     url(r'^$', views.index, name='index_Clientes'),
]