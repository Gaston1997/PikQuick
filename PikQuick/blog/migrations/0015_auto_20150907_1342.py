# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20150907_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='img1',
            field=models.FileField(default=b'null', upload_to=b'img_public', verbose_name='Imagen de portada'),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='img2',
            field=models.FileField(default=b'null', upload_to=b'img_public', verbose_name='Imagen de portada'),
        ),
    ]
