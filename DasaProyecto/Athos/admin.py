from django.contrib import admin
from Athos.models import Profesor,Alumno,Ciclo,Modulo,prof_mod_cic,Nota,Horario,cic_mod_hor,alum_hor

# Register your models here.

admin.site.register(Profesor)
admin.site.register(Alumno)
admin.site.register(Ciclo)
admin.site.register(Modulo)
admin.site.register(prof_mod_cic)
admin.site.register(Nota)
admin.site.register(Horario)
admin.site.register(cic_mod_hor)
admin.site.register(alum_hor)

