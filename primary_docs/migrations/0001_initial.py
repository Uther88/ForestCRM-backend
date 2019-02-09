# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-20 08:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('L', 'Легковой'), ('H', 'Грузовой')], max_length=50, null=True, verbose_name='Тип автомобиля')),
                ('name', models.CharField(max_length=50, verbose_name='Марка автомобиля')),
                ('number', models.CharField(max_length=50, verbose_name='Государственный номерной знак')),
                ('status', models.BooleanField(default=True, verbose_name='Исправен')),
                ('available', models.BooleanField(default=True, verbose_name='Доступный')),
                ('mileage', models.IntegerField(verbose_name='Показания спидометра')),
                ('rate_normal_s', models.FloatField(verbose_name='Расход топлива, лето, норм. усл')),
                ('rate_hard_s', models.FloatField(verbose_name='Расход топлива лето, тяж. усл')),
                ('rate_normal_w', models.FloatField(verbose_name='Расход топлива, зима, норм. усл')),
                ('rate_hard_w', models.FloatField(verbose_name='Расход топлива, зима тяж. усл')),
                ('fuel_balance', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Остаток бензина')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
        migrations.CreateModel(
            name='DriverTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_dest', models.TextField(max_length=150, null=True, verbose_name='Из пункта')),
                ('to_dest', models.TextField(max_length=150, null=True, verbose_name='В пункт')),
                ('departure', models.DateTimeField(verbose_name='Выезд')),
                ('arrival', models.DateTimeField(verbose_name='Возвращение')),
                ('kind', models.CharField(max_length=150, verbose_name='Вид работы')),
                ('distance', models.IntegerField(blank=True, null=True, verbose_name='Расстояние, км.')),
                ('conditions', models.CharField(choices=[('SN', 'Лето, нормальные'), ('SH', 'Лето, тяжелые'), ('WN', 'Зима, нормальные'), ('WH', 'Зима, тяжелые')], max_length=2, verbose_name='Условия')),
                ('total_fuel', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Итого литров бензина')),
            ],
            options={
                'verbose_name': 'Задание для водителя',
                'verbose_name_plural': 'Задания для водителя',
            },
        ),
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=50, verbose_name='Марка топлива')),
                ('code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Код топдива')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Цена за литр')),
            ],
            options={
                'verbose_name': 'Топливо',
                'verbose_name_plural': 'Топливо',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('description', models.TextField(max_length=250, null=True, verbose_name='Полное название')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
            },
        ),
        migrations.CreateModel(
            name='Outfit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime(2018, 6, 20, 8, 32, 28, 21111), verbose_name='Дата')),
                ('place', models.CharField(max_length=50, verbose_name='Место работы')),
                ('forestry', models.CharField(max_length=100, verbose_name='Лесничество')),
                ('mechanism', models.CharField(blank=True, max_length=100, verbose_name='Вид механизма')),
                ('conditions', models.IntegerField(verbose_name='Условия труда')),
                ('task', models.CharField(blank=True, max_length=50, verbose_name='Задание на месяц')),
                ('begin', models.DateField(verbose_name='Начало работы')),
                ('end', models.DateField(verbose_name='Окончание работы')),
                ('amount_total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Итого, сумма')),
                ('done_total', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Выработано норм, всего')),
                ('hours_total', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Дней, всего')),
                ('days_total', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Часов, всего')),
                ('quality', models.CharField(choices=[('good', 'Удовлетворительно'), ('bad', 'Неудовлетворительно')], max_length=50, verbose_name='Оценка качества')),
            ],
            options={
                'verbose_name': 'Наряд-Акт',
                'verbose_name_plural': 'Наряд-Акты',
            },
        ),
        migrations.CreateModel(
            name='OutfitEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=500, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
        migrations.CreateModel(
            name='OutfitExpense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('units', models.CharField(choices=[('MC', 'M³'), ('MS', 'M²'), ('P', 'Шт'), ('HE', 'Га'), ('L', 'Л')], max_length=50, verbose_name='Еденицы измерения')),
                ('quantity_norm', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Количество по норме')),
                ('quantity_fact', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Количество по факту')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость, руб.')),
            ],
            options={
                'verbose_name': 'Расход сырья',
                'verbose_name_plural': 'Расходы сырья',
            },
        ),
        migrations.CreateModel(
            name='OutfitPosting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('units', models.CharField(choices=[('MC', 'M³'), ('MS', 'M²'), ('P', 'Шт'), ('HE', 'Га'), ('L', 'Л')], max_length=50, verbose_name='Еденицы измерения')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Приход лесопродукции',
                'verbose_name_plural': 'Приходы лесопродукции',
            },
        ),
        migrations.CreateModel(
            name='OutfitTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(verbose_name='Разряд')),
                ('workdays', jsonfield.fields.JSONField(default={}, verbose_name='Рабочие Дни')),
                ('hours', models.IntegerField(verbose_name='Всего часов')),
                ('days', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Всего дней')),
                ('tariff_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Тарифная ставка, коэффициент')),
                ('sum_of_coefficients', models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Сумма коэффициентов')),
                ('done', models.DecimalField(decimal_places=1, max_digits=6, verbose_name='Выполнено норм')),
                ('deal_pricing', models.DecimalField(blank=True, decimal_places=2, max_digits=8, verbose_name='По сдел. расц.')),
                ('festive', models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Праздничными')),
                ('bonus', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Премия')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Всего')),
            ],
            options={
                'verbose_name': 'Табель',
                'verbose_name_plural': 'Табеля',
            },
        ),
        migrations.CreateModel(
            name='OutfitWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('units', models.CharField(choices=[('MC', 'M³'), ('MS', 'M²'), ('P', 'Шт'), ('HE', 'Га'), ('L', 'Л')], max_length=50, verbose_name='Еденицы измерения')),
                ('rate', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Нормы выработки')),
                ('done', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Выполнено')),
                ('paragraph', models.CharField(max_length=50, verbose_name='Параграф правочника норм')),
                ('done_norms', models.DecimalField(decimal_places=1, max_digits=8, verbose_name='Выполнено норм')),
                ('pricing', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Расценка, руб.')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Сумма, руб.')),
                ('man_days', models.DecimalField(blank=True, decimal_places=1, max_digits=8, verbose_name='Человеко-дней.')),
                ('auto_days', models.DecimalField(blank=True, decimal_places=1, max_digits=8, verbose_name='Машино-смен')),
                ('days', models.DecimalField(decimal_places=1, max_digits=8, verbose_name='Количество дней.')),
            ],
            options={
                'verbose_name': 'Работа для наряда',
                'verbose_name_plural': 'Работы для наряда',
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Наименование участка')),
                ('series', models.IntegerField(verbose_name='Серия')),
            ],
            options={
                'verbose_name': 'Участок',
                'verbose_name_plural': 'Участки',
            },
        ),
        migrations.CreateModel(
            name='Waybill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of', models.CharField(choices=[('L', 'легкового автомобиля'), ('H', 'грузового автомобиля')], max_length=50, null=True, verbose_name='Тип путевого листа')),
                ('number', models.CharField(max_length=50, verbose_name='Номер')),
                ('date', models.DateField(max_length=50, verbose_name='Дата')),
                ('period_from', models.DateField(blank=True, null=True, verbose_name='Действует с')),
                ('period_to', models.DateField(blank=True, null=True, verbose_name='Действует по')),
                ('dep_date', models.DateTimeField(verbose_name='Выезд из гаража')),
                ('dep_km', models.IntegerField(verbose_name='Показания спидометра, км')),
                ('dep_fact', models.DateTimeField(verbose_name='Фактическое время')),
                ('ret_date', models.DateTimeField(blank=True, null=True, verbose_name='Возвращение в гараж')),
                ('ret_km', models.IntegerField(blank=True, null=True, verbose_name='Показания спидометра, км')),
                ('ret_fact', models.DateTimeField(blank=True, null=True, verbose_name='Фактическое время')),
                ('fuel', models.CharField(max_length=10, verbose_name='Марка горючего')),
                ('fuel_issued', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True, verbose_name='Выданно, л')),
                ('fuel_balance_on_dep', models.DecimalField(decimal_places=2, max_digits=7, null=True, verbose_name='Остаток, выезд')),
                ('fuel_balance_on_ret', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Остаток, возвращение')),
                ('total_km', models.IntegerField(blank=True, default=0, null=True, verbose_name='Итого километров')),
                ('total_hours', models.IntegerField(blank=True, default=0, null=True, verbose_name='Всего часов')),
                ('total_fuel', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True, verbose_name='Итого литров бензина')),
                ('comment', models.TextField(blank=True, max_length=250, verbose_name='Особые отметки')),
                ('is_completed', models.BooleanField(default=False, verbose_name='Завершено')),
            ],
            options={
                'verbose_name': 'Путевой лист',
                'verbose_name_plural': 'Путевые листы',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=50, verbose_name='Отчество')),
                ('position', models.CharField(max_length=50, verbose_name='Должность')),
                ('level', models.CharField(choices=[('1', 'Начальники'), ('2', 'Мастера'), ('3', 'Рабочие')], default=3, max_length=50, null=True, verbose_name='Категория должности')),
                ('station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workers', to='primary_docs.Station', verbose_name='Участок')),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работники',
            },
        ),
    ]