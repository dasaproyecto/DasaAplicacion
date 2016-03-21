from django.shortcuts import render,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from Athos.models import prof_mod_cic,Profesor,cic_mod_hor,Horario
import datetime
import calendar

# Create your views here.

def indice(request):
	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return HttpResponseRedirect("/principal")
	else:
		form = AuthenticationForm()
	return render(request,'Athos/login.html', {'form': form,})  

def logoutpage(request):
	logout(request)
	return HttpResponseRedirect("/")

def principal(request):
	now = datetime.datetime.now().isoweekday()
	profesor = Profesor.objects.filter(user=request.user)	
	lista_modulos = prof_mod_cic.objects.filter(profesores__in=profesor).values("modulos")
	lista_ciclos = prof_mod_cic.objects.filter(profesores__in=profesor).values("ciclos").distinct()
	#for modulo in lista_ciclos:
	#	print(modulo)
	cmhs = Horario.objects.filter(dia_semana=now,cic_mod_hor__modulos__in=lista_modulos,cic_mod_hor__ciclos__in=lista_ciclos).values("hora","dia_semana","cic_mod_hor__modulos__nombre","cic_mod_hor__ciclos__nombre").order_by("hora")
		#cmhs = cic_mod_hor.objects.filter(modulos=modulo.modulos,ciclos=modulo.ciclos,horarios__dia_semana=now)
	lista_horario=[]
	for cmh in cmhs:
		print(cmh)
		
		#	horarios = cmh.horarios.all()
		#	for horario in horarios:
		#		print(horario.hora)
		#		print(horario.dia_semana)
		
		
	return HttpResponse(now)
	

    


	
	
