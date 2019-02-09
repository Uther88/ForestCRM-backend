# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-21 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primary_docs', '0023_auto_20180918_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='nakopitelnayavedomost',
            name='importance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Оплата: ответственные работы'),
        ),
        migrations.AddField(
            model_name='outfit',
            name='amount_importance',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='Итого, по ответственным работам'),
        ),
        migrations.AddField(
            model_name='outfit',
            name='importance',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Ответственные работы'),
        ),
        migrations.AddField(
            model_name='svodnayavedomost',
            name='importance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Оплата: ответственные работы'),
        ),
        migrations.AddField(
            model_name='tractorregform',
            name='amount_importance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Оплата: ответственные работы'),
        ),
        migrations.AddField(
            model_name='tractorregform',
            name='importance',
            field=models.IntegerField(blank=True, null=True, verbose_name='Ответственные работы'),
        ),
        migrations.AlterField(
            model_name='nakopitelnayavedomost',
            name='complexity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Оплата: сложность (условия труда)'),
        ),
        migrations.AlterField(
            model_name='svodnayavedomost',
            name='complexity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Оплата: сложность (условия труда)'),
        ),
    ]
