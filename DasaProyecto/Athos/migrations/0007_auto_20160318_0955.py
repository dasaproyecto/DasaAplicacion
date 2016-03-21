# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Athos', '0006_auto_20160318_0929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cic_mod_hor',
            name='horarios',
        ),
        migrations.AddField(
            model_name='cic_mod_hor',
            name='horarios',
            field=models.ManyToManyField(null=True, to='Athos.Horario'),
        ),
        migrations.RemoveField(
            model_name='prof_mod_cic',
            name='profesores',
        ),
        migrations.AddField(
            model_name='prof_mod_cic',
            name='profesores',
            field=models.ManyToManyField(null=True, to='Athos.Profesor'),
        ),
    ]
