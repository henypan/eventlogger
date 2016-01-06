# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='frequencies',
            field=models.IntegerField(verbose_name='Frequencies', default=0),
        ),
    ]
