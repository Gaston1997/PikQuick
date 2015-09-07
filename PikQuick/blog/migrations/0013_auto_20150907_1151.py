# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20150904_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.FileField(default=b'null', upload_to=b'documents', verbose_name='Imagen de portada')),
            ],
            options={
                'verbose_name': 'Imagen',
                'verbose_name_plural': 'Todas las Imagenes',
            },
        ),
        migrations.RemoveField(
            model_name='entrada',
            name='img',
        ),
        migrations.AddField(
            model_name='imagen',
            name='post',
            field=models.ForeignKey(to='blog.Entrada'),
        ),
    ]
