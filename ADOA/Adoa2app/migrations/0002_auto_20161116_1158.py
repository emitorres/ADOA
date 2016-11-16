# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adoa2app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objetoaprendizaje',
            name='Usuario',
            field=models.ForeignKey(default=1, to='Adoa2app.Usuario'),
            preserve_default=True,
        ),
    ]
