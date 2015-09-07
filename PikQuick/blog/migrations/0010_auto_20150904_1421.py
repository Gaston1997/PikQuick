# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20150904_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='img',
            field=models.FileField(default=b'null', upload_to=b'documents', verbose_name='Imagen de portada'),
        ),
        migrations.DeleteModel(
            name='Imagen',
        ),
    ]
