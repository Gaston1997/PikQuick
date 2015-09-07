# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagen',
            name='published_in',
        ),
        migrations.DeleteModel(
            name='Imagen',
        ),
    ]
