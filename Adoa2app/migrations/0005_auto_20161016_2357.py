# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adoa2app', '0004_auto_20161016_2336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evaluacionitem',
            old_name='enunciado',
            new_name='pregunta',
        ),
    ]
