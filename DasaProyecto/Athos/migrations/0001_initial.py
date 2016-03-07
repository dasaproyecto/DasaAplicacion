# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alum_hor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('DNI', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=30)),
                ('ciudad', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='cic_mod_hor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ciclo',
            fields=[
                ('nombre', models.CharField(max_length=30)),
                ('cod_ciclo', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('hora', models.CharField(max_length=30)),
                ('dia_semana', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('nombre', models.CharField(max_length=30)),
                ('cod_modulo', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('ev', models.CharField(max_length=30)),
                ('nota', models.CharField(max_length=30)),
                ('alumno', models.ManyToManyField(to='Athos.Alumno')),
                ('ciclos', models.ManyToManyField(to='Athos.Ciclo')),
                ('modulos', models.ManyToManyField(to='Athos.Modulo')),
            ],
        ),
        migrations.CreateModel(
            name='prof_mol_cic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('ciclos', models.ManyToManyField(to='Athos.Ciclo')),
                ('modulos', models.ManyToManyField(to='Athos.Modulo')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('DNI', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=30)),
                ('ciudad', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='prof_mol_cic',
            name='profesores',
            field=models.ManyToManyField(to='Athos.Profesor'),
        ),
        migrations.AddField(
            model_name='cic_mod_hor',
            name='ciclos',
            field=models.ManyToManyField(to='Athos.Ciclo'),
        ),
        migrations.AddField(
            model_name='cic_mod_hor',
            name='horarios',
            field=models.ManyToManyField(to='Athos.Horario'),
        ),
        migrations.AddField(
            model_name='cic_mod_hor',
            name='modulos',
            field=models.ManyToManyField(to='Athos.Modulo'),
        ),
        migrations.AddField(
            model_name='alum_hor',
            name='alumno',
            field=models.ForeignKey(to='Athos.Alumno'),
        ),
        migrations.AddField(
            model_name='alum_hor',
            name='horario',
            field=models.ForeignKey(to='Athos.Horario'),
        ),
    ]
