# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adoa2app', '0003_auto_20161012_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluacionitem',
            name='Evaluacion',
            field=models.ForeignKey(to='Adoa2app.Evaluacion', null=True),
            preserve_default=True,
        ),
    ]
