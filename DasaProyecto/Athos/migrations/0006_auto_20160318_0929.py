# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Athos', '0005_profesor_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cic_mod_hor',
            name='ciclos',
        ),
        migrations.AddField(
            model_name='cic_mod_hor',
            name='ciclos',
            field=models.ForeignKey(null=True, to='Athos.Ciclo'),
        ),
        migrations.RemoveField(
            model_name='cic_mod_hor',
            name='horarios',
        ),
        migrations.AddField(
            model_name='cic_mod_hor',
            name='horarios',
            field=models.ForeignKey(null=True, to='Athos.Horario'),
        ),
        migrations.RemoveField(
            model_name='cic_mod_hor',
            name='modulos',
        ),
        migrations.AddField(
            model_name='cic_mod_hor',
            name='modulos',
            field=models.ForeignKey(null=True, to='Athos.Modulo'),
        ),
        migrations.RemoveField(
            model_name='nota',
            name='alumno',
        ),
        migrations.AddField(
            model_name='nota',
            name='alumno',
            field=models.ForeignKey(null=True, to='Athos.Alumno'),
        ),
        migrations.RemoveField(
            model_name='nota',
            name='ciclos',
        ),
        migrations.AddField(
            model_name='nota',
            name='ciclos',
            field=models.ForeignKey(null=True, to='Athos.Ciclo'),
        ),
        migrations.RemoveField(
            model_name='nota',
            name='modulos',
        ),
        migrations.AddField(
            model_name='nota',
            name='modulos',
            field=models.ForeignKey(null=True, to='Athos.Modulo'),
        ),
        migrations.RemoveField(
            model_name='prof_mod_cic',
            name='ciclos',
        ),
        migrations.AddField(
            model_name='prof_mod_cic',
            name='ciclos',
            field=models.ForeignKey(null=True, to='Athos.Ciclo'),
        ),
        migrations.RemoveField(
            model_name='prof_mod_cic',
            name='modulos',
        ),
        migrations.AddField(
            model_name='prof_mod_cic',
            name='modulos',
            field=models.ForeignKey(null=True, to='Athos.Modulo'),
        ),
        migrations.RemoveField(
            model_name='prof_mod_cic',
            name='profesores',
        ),
        migrations.AddField(
            model_name='prof_mod_cic',
            name='profesores',
            field=models.ForeignKey(null=True, to='Athos.Profesor'),
        ),
    ]
