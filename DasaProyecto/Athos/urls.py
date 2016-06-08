from django.conf.urls import url
from Athos import views

urlpatterns = [
   url(r'^$', views.indice, name='indice'),
	url(r'^logout$', views.logoutpage, name='logout'),
	url(r'^principal$', views.principal, name='principal'),
	url(r'^faltas/(?P<modulo_id>\d+)/(?P<ciclo_id>\d+)/(?P<hora>\d+)/$', views.faltas, name='faltas'),

]
