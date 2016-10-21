# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'Actividad',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Asociacion',
            fields=[
                ('actividad_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='Adoa2app.Actividad')),
                ('enunciado', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Asociacion',
            },
            bases=('Adoa2app.actividad',),
        ),
        migrations.CreateModel(
            name='AsociacionItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('campo1', models.CharField(max_length=200)),
                ('campo2', models.CharField(max_length=200)),
                ('asociacion', models.ForeignKey(to='Adoa2app.Asociacion')),
            ],
            options={
                'db_table': 'AsociacionItem',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enunciado', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Evaluacion',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EvaluacionItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enunciado', models.CharField(max_length=200)),
                ('respuestaCorrecta', models.CharField(max_length=200)),
                ('respuestaIncorrecta1', models.CharField(max_length=200)),
                ('respuestaIncorrecta2', models.CharField(max_length=200)),
                ('evaluacion', models.ForeignKey(to='Adoa2app.Evaluacion')),
            ],
            options={
                'db_table': 'EvaluacionItem',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Identificacion',
            fields=[
                ('actividad_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='Adoa2app.Actividad')),
                ('enunciado', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Identificacion',
            },
            bases=('Adoa2app.actividad',),
        ),
        migrations.CreateModel(
            name='IdentificacionItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('texto', models.CharField(max_length=200)),
                ('respuesta', models.BooleanField()),
                ('Identificacion', models.ForeignKey(to='Adoa2app.Identificacion')),
            ],
            options={
                'db_table': 'IdentificacionItem',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ObjetoAprendizaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=300)),
                ('descripcion', models.CharField(max_length=300)),
                ('introduccion', models.CharField(max_length=2000)),
                ('evaluacion', models.OneToOneField(null=True, to='Adoa2app.Evaluacion')),
            ],
            options={
                'db_table': 'ObjetoAprendizaje',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ordenamiento',
            fields=[
                ('actividad_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='Adoa2app.Actividad')),
                ('enunciado', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Ordenamiento',
            },
            bases=('Adoa2app.actividad',),
        ),
        migrations.CreateModel(
            name='OrdenamientoItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('texto', models.CharField(max_length=200)),
                ('orden', models.IntegerField()),
                ('Ordenamiento', models.ForeignKey(to='Adoa2app.Ordenamiento')),
            ],
            options={
                'db_table': 'OrdenamientoItem',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PatronPedagogico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('actividadSugerida', models.CharField(max_length=2, choices=[(b'1', b'VerdaderoFalso'), (b'2', b'Asociacion'), (b'3', b'Video'), (b'4', b'Ordenamiento'), (b'5', b'Identificacion')])),
            ],
            options={
                'db_table': 'PatronPedagogico',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SeccionContenido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contenido', models.CharField(max_length=2000)),
                ('ObjetoAprendizaje', models.ForeignKey(to='Adoa2app.ObjetoAprendizaje')),
            ],
            options={
                'db_table': 'SeccionContenido',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SeccionNombre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('patronPedagogico', models.ForeignKey(to='Adoa2app.PatronPedagogico')),
            ],
            options={
                'db_table': 'SeccionNombre',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VerdaderoFalso',
            fields=[
                ('actividad_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='Adoa2app.Actividad')),
                ('enunciado', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'VerdaderoFalso',
            },
            bases=('Adoa2app.actividad',),
        ),
        migrations.CreateModel(
            name='VerdaderoFalsoItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('afirmacion', models.CharField(max_length=200)),
                ('respuesta', models.BooleanField()),
                ('asociacion', models.ForeignKey(to='Adoa2app.VerdaderoFalso')),
            ],
            options={
                'db_table': 'VerdaderoFalsoItem',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('actividad_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='Adoa2app.Actividad')),
                ('descripcion', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Video',
            },
            bases=('Adoa2app.actividad',),
        ),
        migrations.AddField(
            model_name='seccioncontenido',
            name='seccion',
            field=models.ForeignKey(to='Adoa2app.SeccionNombre'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='objetoaprendizaje',
            name='patronPedagogico',
            field=models.ForeignKey(to='Adoa2app.PatronPedagogico', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actividad',
            name='objetoAprendizaje',
            field=models.ForeignKey(to='Adoa2app.ObjetoAprendizaje'),
            preserve_default=True,
        ),
    ]
