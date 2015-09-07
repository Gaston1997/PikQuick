# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150904_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrada',
            name='autor',
        ),
    ]
