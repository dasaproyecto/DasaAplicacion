from django.conf.urls import url
from Athos import views

urlpatterns = [
   url(r'^$', views.indice, name='indice'),
	url(r'logout$', views.logoutpage, name='logout'),
	url(r'principal$', views.principal, name='principal'),
]
