# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adoa2app', '0002_auto_20180129_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fotoUrl', models.CharField(max_length=45)),
                ('categoria', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['categoria'],
                'db_table': 'Categoria',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='objetoaprendizaje',
            name='Categoria',
            field=models.ForeignKey(default=1, to='Adoa2app.Categoria'),
            preserve_default=True,
        ),
    ]
