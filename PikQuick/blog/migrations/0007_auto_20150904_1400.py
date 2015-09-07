# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_entrada_autor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.FileField(default=b'null', upload_to=b'documents', verbose_name='Imagen de portada')),
            ],
            options={
                'verbose_name': 'Imagen',
                'verbose_name_plural': 'Todas las Imagenes',
            },
        ),
        migrations.AlterField(
            model_name='entrada',
            name='img',
            field=models.ForeignKey(to='blog.Imagenes'),
        ),
    ]
