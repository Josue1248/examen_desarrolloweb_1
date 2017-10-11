# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre', models.CharField(max_length=200)),
                ('Autor', models.CharField(max_length=200)),
                ('Editorial', models.CharField(max_length=200)),
                ('ISBN', models.CharField(max_length=200)),
                ('Precio', models.FloatField()),
                ('Creado', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
