# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-12-21 16:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('primary_docs', '0035_auto_20181220_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecyclingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(null=True, verbose_name='Дата')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recycling_lists', to=settings.AUTH_USER_MODEL, verbose_name='Составитель')),
                ('station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recycling_lists', to='primary_docs.Station', verbose_name='Участок')),
            ],
        ),
        migrations.AddField(
            model_name='outfit',
            name='recycling_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outfit', to='primary_docs.RecyclingList', verbose_name='Ведомость переработки'),
        ),
    ]
