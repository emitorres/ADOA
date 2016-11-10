# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Adoa2app.validator.VacioValidator


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
                ('nombre', models.TextField()),
                ('enunciado', models.TextField()),
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
                ('campo1', models.TextField()),
                ('campo2', models.TextField()),
                ('Asociacion', models.ForeignKey(to='Adoa2app.Asociacion')),
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
                ('enunciado', models.TextField()),
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
                ('pregunta', models.TextField()),
                ('respuestaCorrecta', models.TextField()),
                ('respuestaIncorrecta1', models.TextField()),
                ('respuestaIncorrecta2', models.TextField()),
                ('ordenRespuestaCorrecta', models.IntegerField()),
                ('ordenRespuestaIncorrecta1', models.IntegerField()),
                ('ordenRespuestaIncorrecta2', models.IntegerField()),
                ('Evaluacion', models.ForeignKey(to='Adoa2app.Evaluacion', null=True)),
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
                ('nombre', models.TextField()),
                ('enunciado', models.TextField()),
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
                ('concepto', models.TextField()),
                ('respuesta', models.BooleanField()),
                ('Identificacion', models.ForeignKey(to='Adoa2app.Identificacion')),
            ],
            options={
                'db_table': 'IdentificacionItem',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['nombre'],
                'db_table': 'Menu',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MenuTipoUsuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('menu', models.ForeignKey(to='Adoa2app.Menu')),
            ],
            options={
                'ordering': ['tipousuario', 'menu'],
                'db_table': 'MenuTipoUsuario',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ObjetoAprendizaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('introduccion', models.TextField()),
                ('Evaluacion', models.OneToOneField(null=True, to='Adoa2app.Evaluacion')),
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
                ('nombre', models.TextField()),
                ('enunciado', models.TextField()),
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
                ('texto', models.TextField()),
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
                ('ActividadSugerida', models.CharField(max_length=2, choices=[(b'1', b'VerdaderoFalso'), (b'2', b'Asociacion'), (b'3', b'Video'), (b'4', b'Ordenamiento'), (b'5', b'Identificacion')])),
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
                ('contenido', models.TextField()),
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
                ('PatronPedagogico', models.ForeignKey(to='Adoa2app.PatronPedagogico')),
            ],
            options={
                'db_table': 'SeccionNombre',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, validators=[Adoa2app.validator.VacioValidator.VacioValidator])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'TipoUsuario',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, validators=[Adoa2app.validator.VacioValidator.VacioValidator])),
                ('apellido', models.CharField(max_length=100, validators=[Adoa2app.validator.VacioValidator.VacioValidator])),
                ('dni', models.CharField(max_length=15)),
                ('carrera', models.CharField(max_length=100)),
                ('clave', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=75)),
                ('estado', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('sexo', models.BooleanField()),
                ('tipousuario', models.ForeignKey(blank=True, to='Adoa2app.TipoUsuario', null=True)),
            ],
            options={
                'ordering': ['tipousuario', 'nombre'],
                'db_table': 'Usuario',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VerdaderoFalso',
            fields=[
                ('actividad_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='Adoa2app.Actividad')),
                ('nombre', models.TextField()),
                ('enunciado', models.TextField()),
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
                ('afirmacion', models.TextField()),
                ('respuesta', models.BooleanField()),
                ('VerdaderoFalso', models.ForeignKey(to='Adoa2app.VerdaderoFalso')),
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
                ('nombre', models.TextField()),
                ('descripcion', models.TextField()),
                ('link', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'Video',
            },
            bases=('Adoa2app.actividad',),
        ),
        migrations.AddField(
            model_name='token',
            name='usuario',
            field=models.ForeignKey(blank=True, to='Adoa2app.Usuario', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='seccioncontenido',
            name='SeccionNombre',
            field=models.ForeignKey(to='Adoa2app.SeccionNombre'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='objetoaprendizaje',
            name='PatronPedagogico',
            field=models.ForeignKey(to='Adoa2app.PatronPedagogico', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='objetoaprendizaje',
            name='Usuario',
            field=models.OneToOneField(default=1, to='Adoa2app.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='menutipousuario',
            name='tipousuario',
            field=models.ForeignKey(to='Adoa2app.TipoUsuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='menu',
            name='tipousuarios',
            field=models.ManyToManyField(to='Adoa2app.TipoUsuario', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actividad',
            name='ObjetoAprendizaje',
            field=models.ForeignKey(to='Adoa2app.ObjetoAprendizaje'),
            preserve_default=True,
        ),
    ]
