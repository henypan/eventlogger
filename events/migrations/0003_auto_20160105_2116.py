# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20160105_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='method',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='question',
            name='note',
            field=models.CharField(default='', max_length=200),
        ),
    ]
