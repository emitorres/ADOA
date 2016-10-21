# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adoa2app', '0008_evaluacionitem_ordenrespuestacorrecta'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluacionitem',
            name='ordenRespuestaIncorrecta1',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evaluacionitem',
            name='ordenRespuestaIncorrecta2',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
