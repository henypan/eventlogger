# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20160105_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='method',
            field=models.CharField(blank=True, max_length=30, default=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='note',
            field=models.CharField(blank=True, max_length=200, default=''),
        ),
    ]
