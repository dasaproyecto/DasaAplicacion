# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Athos', '0002_auto_20160307_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciclo',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
