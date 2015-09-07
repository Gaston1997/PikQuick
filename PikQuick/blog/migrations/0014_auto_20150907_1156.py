# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20150907_1151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagen',
            name='post',
        ),
        migrations.AddField(
            model_name='entrada',
            name='img1',
            field=models.FileField(default=b'null', upload_to=b'documents', verbose_name='Imagen de portada'),
        ),
        migrations.AddField(
            model_name='entrada',
            name='img2',
            field=models.FileField(default=b'null', upload_to=b'documents', verbose_name='Imagen de portada'),
        ),
        migrations.DeleteModel(
            name='Imagen',
        ),
    ]
