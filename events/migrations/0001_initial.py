# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('question_text', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='date published', blank=True)),
                ('number', models.IntegerField(verbose_name='Number')),
                ('difficulty', models.CharField(max_length=30)),
                ('method', models.CharField(max_length=30)),
                ('note', models.CharField(max_length=200)),
                ('frequencies', models.IntegerField(verbose_name='Frequencies')),
            ],
        ),
    ]
