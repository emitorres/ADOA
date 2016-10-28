# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adoa2app', '0007_auto_20161019_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluacionitem',
            name='ordenRespuestaCorrecta',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
