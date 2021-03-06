# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-23 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primary_docs', '0007_auto_20180629_1359'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='outfitevent',
            options={'ordering': ['name'], 'verbose_name': 'Мероприятие', 'verbose_name_plural': 'Мероприятия'},
        ),
        migrations.AlterField(
            model_name='outfitevent',
            name='description',
            field=models.TextField(blank=True, max_length=500, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='outfitevent',
            name='name',
            field=models.CharField(max_length=500, verbose_name='Название'),
        ),
    ]
