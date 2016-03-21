from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Ciclo(models.Model):
	nombre = models.CharField(max_length=100)
	cod_ciclo = models.CharField(primary_key=True, max_length=30)
	
	def __str__(self):
		return '%s' % (self.nombre)

class Profesor(models.Model):
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)
	DNI = models.CharField(primary_key=True,max_length=30)
	direccion = models.CharField(max_length=30)
	email = models.EmailField()
	telefono = models.CharField(max_length=30)
	ciudad = models.CharField(max_length=30)
	user = models.OneToOneField(User,null=True)

	def __str__(self):
		return '%s' % (self.nombre)

class Modulo(models.Model):
	nombre = models.CharField(max_length=100)
	cod_modulo = models.CharField(primary_key=True,max_length=30)
	
	def __str__(self):
		return '%s' % (self.nombre)

class prof_mod_cic(models.Model):
	modulos = models.ForeignKey(Modulo,null=True)
	ciclos = models.ForeignKey(Ciclo,null=True)
	profesores = models.ManyToManyField(Profesor,null=True)

#-------------------------------------------------

class Alumno(models.Model):
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)
	DNI = models.CharField(primary_key=True,max_length=30)
	direccion = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	telefono = models.CharField(max_length=30)
	ciudad = models.CharField(max_length=30)
	

	def __str__(self):
		return '%s' % (self.nombre)


class Nota(models.Model):
	ev = models.CharField(max_length=30)
	nota = models.CharField(max_length=30)
	modulos = models.ForeignKey(Modulo,null=True)
	alumno = models.ForeignKey(Alumno,null=True)
	ciclos = models.ForeignKey(Ciclo,null=True)

#--------------------------------------------------
	

class	Horario(models.Model):
	hora = models.CharField(max_length=30)
	dia_semana = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

	def __str__(self):
		return '%s' % (self.hora + ':' +str(self.dia_semana))

class Meta:
        unique_together = ('hora','dia_semana')

class cic_mod_hor(models.Model):
	ciclos = models.ForeignKey(Ciclo,null=True)
	modulos = models.ForeignKey(Modulo,null=True)
	horarios = models.ManyToManyField(Horario)

class Meta:
        unique_together = ('ciclos','modulos')


#---------------------------------

class alum_hor(models.Model):
	fecha = models.DateField()
	alumno = models.ForeignKey(Alumno)
	horario = models.ForeignKey(Horario)
