# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-03 10:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('primary_docs', '0015_auto_20180903_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='svodnayavedomost',
            name='prep_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата составления'),
        ),
    ]
