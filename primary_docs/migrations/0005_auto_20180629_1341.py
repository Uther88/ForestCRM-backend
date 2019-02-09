# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-29 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primary_docs', '0004_auto_20180629_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outfit',
            name='amount_bonus',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='Итого по премиям'),
        ),
        migrations.AlterField(
            model_name='outfit',
            name='amount_coefficient',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='Итого по коэффициенту'),
        ),
        migrations.AlterField(
            model_name='outfit',
            name='bonus',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=5, verbose_name='Премия'),
        ),
        migrations.AlterField(
            model_name='outfit',
            name='coefficient',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=5, verbose_name='Коэффициент'),
        ),
        migrations.AlterField(
            model_name='outfitwork',
            name='auto_days',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=8, null=True, verbose_name='Машино-смен'),
        ),
    ]
