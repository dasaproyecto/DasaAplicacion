# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Athos', '0007_auto_20160318_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cic_mod_hor',
            name='horarios',
            field=models.ManyToManyField(to='Athos.Horario'),
        ),
    ]
