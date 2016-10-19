# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adoa2app', '0005_auto_20161016_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asociacion',
            name='enunciado',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asociacionitem',
            name='campo1',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asociacionitem',
            name='campo2',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluacion',
            name='enunciado',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluacionitem',
            name='pregunta',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluacionitem',
            name='respuestaCorrecta',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluacionitem',
            name='respuestaIncorrecta1',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluacionitem',
            name='respuestaIncorrecta2',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='identificacion',
            name='enunciado',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='identificacionitem',
            name='concepto',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='objetoaprendizaje',
            name='descripcion',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='objetoaprendizaje',
            name='introduccion',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='objetoaprendizaje',
            name='titulo',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ordenamiento',
            name='enunciado',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ordenamientoitem',
            name='texto',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='seccioncontenido',
            name='contenido',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='verdaderofalso',
            name='enunciado',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='verdaderofalsoitem',
            name='afirmacion',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='video',
            name='link',
            field=models.CharField(max_length=300),
            preserve_default=True,
        ),
    ]
