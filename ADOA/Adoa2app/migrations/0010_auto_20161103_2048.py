# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adoa2app', '0009_auto_20161026_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='asociacion',
            name='nombre',
            field=models.TextField(default='Asociacion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='identificacion',
            name='nombre',
            field=models.TextField(default='Identificacion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordenamiento',
            name='nombre',
            field=models.TextField(default='Ordenamiento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='verdaderofalso',
            name='nombre',
            field=models.TextField(default='Verdadero o Falso'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='nombre',
            field=models.TextField(default='Video'),
            preserve_default=False,
        ),
    ]
