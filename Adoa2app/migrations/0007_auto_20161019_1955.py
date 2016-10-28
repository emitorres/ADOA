# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adoa2app', '0006_auto_20161019_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='descripcion',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
