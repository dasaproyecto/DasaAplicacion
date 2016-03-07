from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Ciclo(models.Model):
	nombre = models.CharField(max_length=30)
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

	def __str__(self):
		return '%s' % (self.nombre)

class Modulo(models.Model):
	nombre = models.CharField(max_length=30)
	cod_modulo = models.CharField(primary_key=True,max_length=30)
	
	def __str__(self):
		return '%s' % (self.nombre)

class prof_mol_cic(models.Model):
	modulos = models.ManyToManyField(Modulo)
	ciclos = models.ManyToManyField(Ciclo)
	profesores = models.ManyToManyField(Profesor)

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
	modulos = models.ManyToManyField(Modulo)
	alumno = models.ManyToManyField(Alumno)
	ciclos = models.ManyToManyField(Ciclo)

#--------------------------------------------------
	

class	Horario(models.Model):
	hora = models.CharField(max_length=30)
	dia_semana = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

class Meta:
        unique_together = ('hora','dia_semana')

class cic_mod_hor(models.Model):
	ciclos = models.ManyToManyField(Ciclo)
	modulos = models.ManyToManyField(Modulo)
	horarios = models.ManyToManyField(Horario)

#---------------------------------

class alum_hor(models.Model):
	fecha = models.DateField()
	alumno = models.ForeignKey(Alumno)
	horario = models.ForeignKey(Horario)
