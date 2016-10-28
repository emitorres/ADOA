# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adoa2app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actividad',
            old_name='objetoAprendizaje',
            new_name='ObjetoAprendizaje',
        ),
        migrations.RenameField(
            model_name='asociacionitem',
            old_name='asociacion',
            new_name='Asociacion',
        ),
        migrations.RenameField(
            model_name='evaluacionitem',
            old_name='evaluacion',
            new_name='Evaluacion',
        ),
        migrations.RenameField(
            model_name='objetoaprendizaje',
            old_name='evaluacion',
            new_name='Evaluacion',
        ),
        migrations.RenameField(
            model_name='objetoaprendizaje',
            old_name='patronPedagogico',
            new_name='PatronPedagogico',
        ),
        migrations.RenameField(
            model_name='patronpedagogico',
            old_name='actividadSugerida',
            new_name='ActividadSugerida',
        ),
        migrations.RenameField(
            model_name='seccioncontenido',
            old_name='seccion',
            new_name='SeccionNombre',
        ),
        migrations.RenameField(
            model_name='seccionnombre',
            old_name='patronPedagogico',
            new_name='PatronPedagogico',
        ),
        migrations.RenameField(
            model_name='verdaderofalsoitem',
            old_name='asociacion',
            new_name='VerdaderoFalso',
        ),
    ]
