# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adoa2app', '0002_auto_20161008_1620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='identificacionitem',
            old_name='texto',
            new_name='concepto',
        ),
    ]
