# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adoa2app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asociacionitem',
            name='ordenCampo1',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asociacionitem',
            name='ordenCampo2',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(unique=True, max_length=75, error_messages={b'unique': b'El e-mail propocionado est\xc3\xa1 en uso. <br> Por favor, ingrese uno diferente.'}),
            preserve_default=True,
        ),
        migrations.AlterModelTable(
            name='token',
            table='Token',
        ),
    ]
