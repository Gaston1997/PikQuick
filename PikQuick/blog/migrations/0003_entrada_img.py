# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150831_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='img',
            field=models.FileField(default=b'null', upload_to=b'static/img_public', verbose_name='Imagen de portada'),
        ),
    ]
