from django.shortcuts import render,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from Athos.models import prof_mod_cic,Profesor,cic_mod_hor,Horario,Nota,Alumno,alum_hor
import datetime
import calendar
from django.http import QueryDict

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
	request.session["fecha"]=datetime.datetime.now()
	request.session["dia_semana"]=now
	profesor = Profesor.objects.filter(user=request.user)	
	lista_modulos = prof_mod_cic.objects.filter(profesores__in=profesor).values("modulos")
	lista_ciclos = prof_mod_cic.objects.filter(profesores__in=profesor).values("ciclos").distinct()
	#for modulo in lista_ciclos:
	#	print(modulo)
	cmhs = Horario.objects.filter(dia_semana=now,cic_mod_hor__modulos__in=lista_modulos,cic_mod_hor__ciclos__in=lista_ciclos).values("hora","dia_semana","cic_mod_hor__modulos__nombre","cic_mod_hor__modulos","cic_mod_hor__ciclos__nombre","cic_mod_hor__ciclos").order_by("hora")
		#cmhs = cic_mod_hor.objects.filter(modulos=modulo.modulos,ciclos=modulo.ciclos,horarios__dia_semana=now)
	lista_horario=[]
	for cmh in cmhs:
		print(cmh)
		
		#	horarios = cmh.horarios.all()
		#	for horario in horarios:
		#		print(horario.hora)
		#		print(horario.dia_semana)
		
		
	return render(request,'Athos/principal.html', {'cmhs': cmhs,})

def faltas(request,ciclo_id,modulo_id,hora): #fmc= falta_modulo_cliclo
	if request.method == 'POST':
		faltas = request.POST.getlist('ck_alumno')
		for falta in faltas:
			horario=Horario.objects.filter(hora=request.session["hora"],dia_semana=request.session["dia_semana"])
			alumno = get_object_or_404(Alumno, pk=falta)
			falta = alum_hor(fecha=request.session["fecha"],horario=horario[0],alumno=alumno)
			falta.save()
	else:
		request.session["hora"]=hora
		request.session["ciclo"]=ciclo_id
		request.session["modulo"]=modulo_id
		fmc = Nota.objects.filter(ciclos=ciclo_id,modulos=modulo_id).values("ev","nota","ciclos__nombre","modulos__nombre","alumno__nombre","alumno__DNI")
		return render(request,'Athos/faltas.html',{'fmc':fmc,})
	
	return HttpResponseRedirect("/principal")













	

    


	
	
