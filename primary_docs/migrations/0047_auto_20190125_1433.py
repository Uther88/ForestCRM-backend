# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-01-25 14:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('primary_docs', '0046_outfit_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short', models.CharField(max_length=50, null=True, unique=True, verbose_name='Название')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Еденица измерения',
                'verbose_name_plural': 'Еденицы измерения',
            },
        ),
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['name', 'kind'], 'verbose_name': 'Автомобиль', 'verbose_name_plural': 'Автомобили'},
        ),
        migrations.AlterField(
            model_name='material',
            name='units',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='materials', to='primary_docs.Units', verbose_name='Еденицы измерения'),
        ),
        migrations.AlterField(
            model_name='outfitwork',
            name='units',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='outfit_works', to='primary_docs.Units', verbose_name='Еденицы измерения'),
        ),
        migrations.AlterField(
            model_name='tractorregformwork',
            name='units',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='regform_works', to='primary_docs.Units', verbose_name='Еденицы измерения'),
        ),
    ]
