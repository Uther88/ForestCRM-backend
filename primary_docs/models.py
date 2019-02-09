import json

from django.utils import timezone
from django.db import models
from django.db.models import Q
from django.conf import settings
from django.dispatch import receiver
from django.core.serializers.json import DjangoJSONEncoder

from jsonfield import JSONField


# Departaments / Отделы
DEPARTAMENTS = (
        ('les', 'Лес'),
        ('ceh', 'Цех'),
        ('phs', 'ПХС'),
        ('mtm', 'МТМ')
    )


# Fuel distribution types / Типы отчетов распределения ГСМ
CHOICES_OF_FUEL_DISTRIBUTION = (
    ('OF', 'Наряд-акт'),
    ('WB', 'Путевой лист'),
    ('TR', 'Учетный лист тракториста'),
)

# Types of venichle / Типы транспортных устройств
CHOICES_OF_KIND = (
        ('L', 'Легковой'),
        ('H', 'Грузовой'),
        ('T', 'Трактор'),
        ('C', 'Цистерна'),
        ('S', 'Шасси'),
        ('P', 'Прицеп'),
    )

# Organization model / Модель организации
class Organization(models.Model):
    head = models.ForeignKey(
        'primary_docs.Worker',
        related_name="organization_head",
        verbose_name="Руководитель",
        null=True,
        on_delete=models.SET_NULL,
        blank=True
        )
    name = models.CharField('Название', max_length=150)
    description = models.TextField('Полное название', max_length=250, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


class Units(models.Model):
    short = models.CharField('Название', max_length=50, unique=True, null=True)
    name = models.CharField('Описание', max_length=50, null=True)

    class Meta:
        verbose_name = 'Еденица измерения'
        verbose_name_plural = 'Еденицы измерения'

    def __str__(self):
        return self.name


# Model of positions / Модель должностей
class Position(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name


# Model of station / Модель участка
class Station(models.Model):
    name = models.CharField('Наименование участка', max_length=250)
    series = models.IntegerField('Серия')
    organization = models.ForeignKey(
        Organization,
        related_name='stations',
        verbose_name='Организация',
        null=True,
        on_delete=models.SET_NULL
    )
    head = models.ForeignKey(
        'primary_docs.Worker',
        related_name='sub_stations',
        verbose_name='Начальник участка',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    masters = models.ManyToManyField(
        'primary_docs.Worker',
        related_name='master_of_stations',
        verbose_name='Мастер участка',
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Участок'
        verbose_name_plural = 'Участки'


# Model of worker / Модель работника
class Worker(models.Model):
    LEVELS = (
        ('1', 'Начальники'),
        ('2', 'Мастера'),
        ('3', 'Рабочие'),
    )
    surname = models.CharField('Фамилия', max_length=50)
    name = models.CharField('Имя', max_length=50)
    patronymic = models.CharField('Отчество', max_length=50)
    position = models.ForeignKey(
            Position,
            related_name="workers",
            verbose_name="Должность",
            null=True,
            on_delete=models.PROTECT
        )
    level = models.CharField(
        'Категория должности',
        max_length=50,
        choices=LEVELS,
        default=3,
        null=True
    )
    rank = models.IntegerField('Разряд', blank=True, null=True)
    station = models.ForeignKey(
        Station,
        related_name='workers',
        verbose_name='Участок',
        null=True,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.surname + ' ' + self.name + ' ' + self.patronymic

    @property
    def get_full_name(self):
        return '{} {} {}'.format(self.surname, self.name, self.patronymic)

    @property
    def get_short_full_name(self):
        return '{} {}.{}.'.format(self.surname, self.name[0], self.patronymic[0])

    def get_position(self):
        return self.position.name

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
        ordering = ['surname']


# Model of fuel / Модель топлива
class Fuel(models.Model):
    mark = models.CharField(
        'Марка топлива',
        max_length=50
    )
    code = models.CharField(
        'Код топдива',
        max_length=50,
        blank=True,
        null=True,
    )
    price = models.DecimalField(
        'Цена за литр',
        max_digits=5,
        decimal_places=2,
        null=True
    )

    def __str__(self):
        if self.code:
            return '{} - {}'.format(self.mark, self.code)
        return self.mark

    def get_full(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Топливо'
        verbose_name_plural = 'Топливо'


# Model of car / Модель автомобиля
class Car(models.Model):
    kind = models.CharField(
        'Тип автомобиля',
        choices=CHOICES_OF_KIND,
        max_length=50,
        null=True
    )
    name = models.CharField(
        'Марка автомобиля',
        max_length=50
    )
    number = models.CharField(
        'Государственный номерной знак',
        max_length=50,
        blank=True,
        null=True
    )
    status = models.BooleanField(
        'Исправен',
        default=True
    )
    available = models.BooleanField('Доступный', default=True)
    mileage = models.IntegerField('Показания спидометра', default=0)
    rate_normal_s = models.FloatField('Расход топлива, лето, норм. усл', default=0)
    rate_hard_s = models.FloatField('Расход топлива лето, тяж. усл', default=0)
    rate_normal_w = models.FloatField('Расход топлива, зима, норм. усл', default=0)
    rate_hard_w = models.FloatField('Расход топлива, зима тяж. усл', default=0)

    station = models.ForeignKey(
        Station,
        related_name='cars',
        verbose_name='Участок',
        null=True,
        on_delete=models.SET_NULL
    )
    fuel_balance = models.DecimalField(
        'Остаток бензина',
        max_digits=7,
        decimal_places=2,
        default=0
    )
    fuel = models.ForeignKey(
        Fuel,
        related_name='cars',
        verbose_name='Топливо',
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return '{}: {}, номер: {}'.format(self.get_kind_display(), self.name, self.number or 'нет')

    def update_data(self, km=None, fuel=None):
        if km:
            self.mileage = km
        if fuel:
            self.fuel_balance = fuel
        self.available = True
        self.save()

    def full_name(self):
        return '{0} - {1}'.format(self.name, self.number)

    def get_rate(self, conditions):
        if conditions == 'SN':
            return self.rate_normal_s
        elif conditions == 'WN':
            return self.rate_normal_w
        elif conditions == 'SH':
            return self.rate_hard_s
        elif conditions == 'WH':
            return self.rate_hard_w

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        ordering = ['name', 'kind']


# Model of materials / Модель материалов

class MaterialCategory(models.Model):
    name = models.CharField('Наименование', max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория материалов'
        verbose_name_plural = 'Категории материалов'


class Material(models.Model):
    name = models.CharField('Наименование', max_length=100, unique=True)
    units = models.ForeignKey(
        Units,
        related_name="materials",
        verbose_name="Еденицы измерения",
        null=True,
        on_delete=models.SET_NULL
        )
    quantity = models.DecimalField('Количество', max_digits=10, decimal_places=2, default=0)
    category = models.ForeignKey(
        MaterialCategory, 
        related_name="materials",
        verbose_name="Категория",
        blank=True,
        null=True,
        on_delete=models.PROTECT
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


# Outfit events / Мероприятия (работы)

class OutfitEvent(models.Model):
    name = models.CharField('Название', max_length=500)
    description = models.TextField('Описание', max_length=500, blank=True)

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
        ordering = ['name']

    def __str__(self):
        if self.description:
            return '{} ({})'.format(self.name, self.description)
        else:
            return self.name

    def full_name(self):
        return self.__str__()


# Model of waybill / Модель путевого листа
class Waybill(models.Model):
    CHOICES_OF_TYPE = (
        ('L', 'легкового автомобиля'),
        ('H', 'грузового автомобиля'),
    )
    departament = models.CharField(
        'Отдел',
        choices=DEPARTAMENTS,
        max_length=50,
        null=True
        )
    event = models.ForeignKey(
        OutfitEvent,
        related_name="waybills",
        verbose_name="Мероприятие",
        null=True,
        on_delete=models.PROTECT
        )

    type_of = models.CharField(
        'Тип путевого листа',
        choices=CHOICES_OF_TYPE,
        max_length=50,
        null=True
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='waybills',
        verbose_name='Автор',
        null=True,
        on_delete=models.SET_NULL
    )
    station = models.ForeignKey(
        Station,
        related_name='waybills',
        verbose_name='Участок',
        null=True,
        on_delete=models.PROTECT
    )
    number = models.CharField('Номер', max_length=50)
    date = models.DateField('Дата', max_length=50)
    period_from = models.DateField(
        'Действует с',
        blank=True,
        null=True
    )
    period_to = models.DateField(
        'Действует по',
        blank=True,
        null=True
    )
    organization = models.ForeignKey(
        Organization,
        related_name='waybills',
        verbose_name='Организация',
        null=True,
        on_delete=models.PROTECT
    )
    car = models.ForeignKey(
        Car,
        related_name='waybills',
        verbose_name='Автомобиль',
        null=True,
        on_delete=models.PROTECT
    )
    driver = models.ForeignKey(
        Worker,
        related_name='waybills',
        verbose_name='Водитель',
        null=True,
        on_delete=models.PROTECT
    )
    handout = models.ForeignKey(
        'primary_docs.Handout',
        related_name="waybills",
        verbose_name="Раздаточная ведомость",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
        )
    fuel_distribution = models.ForeignKey(
        'primary_docs.FuelDistribution',
        related_name="waybills",
        verbose_name="Распределение ГСМ",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
        )

    # Work of auto and driver / Работа водителя и автомобиля

    # Departure / Выезд
    dep_date = models.DateTimeField('Выезд из гаража')
    dep_km = models.IntegerField('Показания спидометра, км')
    dep_fact = models.DateTimeField('Фактическое время')

    # Return / Возвращение
    ret_date = models.DateTimeField(
        'Возвращение в гараж',
        blank=True,
        null=True
    )
    ret_km = models.IntegerField(
        'Показания спидометра, км',
        blank=True,
        null=True
    )
    ret_fact = models.DateTimeField(
        'Фактическое время',
        blank=True,
        null=True
    )

    # Movement of fuel / Движение горючего
    fuel = models.CharField('Марка горючего', max_length=10)
    fuel_issued = models.DecimalField(
        'Выданно, л',
        max_digits=7,
        decimal_places=2,
        null=True,
        blank=True,
        default=0
    )
    fuel_balance_on_dep = models.DecimalField(
        'Остаток, выезд',
        max_digits=7,
        decimal_places=2,
        null=True
    )
    fuel_balance_on_ret = models.DecimalField(
        'Остаток, возвращение',
        max_digits=7,
        decimal_places=2,
        null=True,
        blank=True
    )

    # Signs / Подписи
    dispatcher = models.ForeignKey(
        Worker,
        related_name='disp_signs',
        verbose_name='Диспетчер',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    check_out_allow = models.ForeignKey(
        Worker,
        related_name='allow_mech_signs',
        verbose_name='Выезд разрешен, механик',
        null=True,
        on_delete=models.PROTECT
    )
    car_took = models.ForeignKey(
        Worker,
        related_name='car_took_signs',
        verbose_name='Автомобиль принял, водитель',
        null=True,
        on_delete=models.PROTECT
    )

    auto_passed = models.ForeignKey(
        Worker,
        related_name='auto_pass_signs',
        verbose_name='Сдал, водитель',
        null=True,
        on_delete=models.PROTECT
    )
    auto_accept = models.ForeignKey(
        Worker,
        related_name='auto_accept_signs',
        verbose_name='Принял, механик',
        null=True,
        on_delete=models.PROTECT
    )

    total_km = models.IntegerField(
        'Итого километров',
        blank=True,
        null=True,
        default=0
    )
    total_hours = models.IntegerField(
        'Всего часов',
        blank=True,
        null=True,
        default=0
    )
    total_fuel = models.DecimalField(
        'Итого литров бензина',
        max_digits=7,
        decimal_places=2,
        null=True,
        blank=True,
        default=0
    )
    comment = models.TextField(
        'Особые отметки',
        max_length=250,
        blank=True
    )
    is_completed = models.BooleanField(
        'Завершено',
        default=False
    )
    conducted = models.BooleanField(
        'Проведен',
        default=False
    )

    def __str__(self):
        return '{} №{}'.format(self.station.name, self.number)

    def complete(self):
        self.car.update_data(self.ret_km, self.fuel_balance_on_ret)
        self.save()

    def conduct(self):
        self.conducted = True
        self.save()


    class Meta:
        verbose_name = 'Путевой лист'
        verbose_name_plural = 'Путевые листы'


# Model of task to driver / Модель задачи для водителя
class DriverTask(models.Model):
    # Choices of conditions type / Выбор значений для погодных условий задачи
    CONDITION_CHOICES = (
        ('SN', 'Лето, нормальные'),
        ('SH', 'Лето, тяжелые'),
        ('WN', 'Зима, нормальные'),
        ('WH', 'Зима, тяжелые')
    )
    customer = models.ForeignKey(
        Station,
        related_name='driver_tasks',
        verbose_name='Заказчик',
        null=True,
        on_delete=models.PROTECT
    )
    from_dest = models.TextField(
        'Из пункта',
        max_length=150,
        null=True
    )
    to_dest = models.TextField(
        'В пункт',
        max_length=150,
        null=True
    )
    car = models.ForeignKey(
        Car,
        related_name='tasks',
        verbose_name='Автомобиль',
        null=True,
        on_delete=models.PROTECT
    )
    departure = models.DateTimeField('Выезд')
    arrival = models.DateTimeField('Возвращение')
    kind = models.CharField('Вид работы', max_length=150)
    distance = models.IntegerField(
        'Расстояние, км.',
        blank=True,
        null=True
    )
    conditions = models.CharField(
        'Условия',
        max_length=2,
        choices=CONDITION_CHOICES
    )
    total_fuel = models.DecimalField(
        'Итого литров бензина',
        max_digits=10,
        decimal_places=2
    )
    waybill = models.ForeignKey(
            Waybill,
            related_name="tasks",
            verbose_name="Путевой лист",
            null=True,
        )

    def calc_total_fuel(self):
        rate = self.car.get_rate(self.conditions)
        return self.distance * rate

    def __str__(self):
        return '{} - {}'.format(self.from_dest, self.to_dest)

    @property
    def get_rate(self):
        rate = self.car.get_rate(self.conditions)
        return rate

    class Meta:
        verbose_name = 'Задание для водителя'
        verbose_name_plural = 'Задания для водителя'


#   Outfit / Наряд - акт на производство работ

class Outfit(models.Model):
    QUALITY_CHOICES = (
        ('good', 'Удовлетворительно'),
        ('bad', 'Неудовлетворительно'),
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='outfits',
        verbose_name='Автор',
        null=True,
        on_delete=models.SET_NULL
    )
    conducted = models.BooleanField(
        'Проведен',
        default=False
    )
    date = models.DateField('Дата', default=timezone.now, blank=True)
    organization = models.ForeignKey(
        Organization,
        related_name="outfits",
        verbose_name="Организация",
        null=True,
        on_delete=models.PROTECT
        )
    place = models.CharField(
        'Место работы', 
        max_length=50, 
        null=True, 
        blank=True
        )
    station = models.ForeignKey(
        Station,
        related_name="outfits",
        verbose_name="Участок",
        null=True,
        on_delete=models.PROTECT
        )
    departament = models.CharField(
        'Отдел',
        choices=DEPARTAMENTS,
        max_length=50,
        null=True
        )
    brigadier = models.ForeignKey(
        Worker,
        related_name='outfit_brigadier',
        verbose_name='Бригадир',
        null=True,
        on_delete=models.SET_NULL
    )
    forestry = models.CharField('Лесничество', max_length=100)
    mechanism = models.CharField('Вид механизма', max_length=100, blank=True)
    event = models.ForeignKey(
        OutfitEvent,
        related_name='outfits',
        verbose_name='Мероприятие',
        null=True,
        on_delete=models.PROTECT
    )
    conditions = models.IntegerField('Условия труда', blank=True, null=True)
    importance = models.IntegerField('Ответственные работы', blank=True, null=True)
    bonus = models.DecimalField(
        'Премия',
        max_digits=5,
        decimal_places=1,
        blank=True,
    )
    coefficient = models.DecimalField(
        'Коэффициент',
        max_digits=5,
        decimal_places=1,
        blank=True,
    )
    task = models.CharField('Задание на месяц', max_length=50, blank=True)
    begin = models.DateField('Начало работы')
    end = models.DateField('Окончание работы')
    quality = models.CharField('Оценка качества', choices=QUALITY_CHOICES, max_length=50)

    done_total = models.DecimalField('Выработано норм, всего', max_digits=5, decimal_places=2)
    amount = models.DecimalField('Итого, сумма', max_digits=10, decimal_places=2)
    amount_conditions = models.DecimalField(
        'Итого, по условиям труда', max_digits=10, decimal_places=2, blank=True, null=True
        )
    amount_importance = models.DecimalField(
        'Итого, по ответственным работам',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )
    amount_coefficient = models.DecimalField(
        'Итого по коэффициенту',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )
    amount_bonus = models.DecimalField(
        'Итого по премиям',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )
    amount_total = models.DecimalField('Всего, сумма', max_digits=10, decimal_places=2)
    hours_total = models.DecimalField('Часов, всего', max_digits=5, decimal_places=1)
    days_total = models.DecimalField('Дней, всего', max_digits=5, decimal_places=1)

    issued = models.ForeignKey(
        Worker,
        related_name='outfit_given',
        verbose_name='Наряд выдан',
        null=True,
        on_delete=models.PROTECT
    )
    accepted = models.ForeignKey(
        Worker,
        related_name='outfit_accept',
        verbose_name='К исполнению принял',
        null=True,
        on_delete=models.PROTECT
    )

    work_passed = models.ForeignKey(
        Worker,
        related_name='outfit_work_passed',
        verbose_name='Работу сдал',
        null=True,
        on_delete=models.PROTECT
    )
    work_accept = models.ForeignKey(
        Worker,
        related_name='outfit_work_accept',
        verbose_name='Работу принял',
        null=True,
        on_delete=models.SET_NULL
    )

    responsible = models.ForeignKey(
        Worker,
        related_name='outfit_responsible',
        verbose_name='Ответственный за ведение табеля',
        null=True,
        on_delete=models.PROTECT
    )
    calculated = models.ForeignKey(
        Worker,
        related_name='outfit_calculate',
        verbose_name='Расчет составил',
        null=True,
        on_delete=models.PROTECT
    )
    deposited = models.ForeignKey(
        Worker,
        related_name='outfit_deposited',
        verbose_name='Принял на ответственное хранение',
        null=True,
        on_delete=models.PROTECT
    )

    recycling_list = models.ForeignKey(
        'primary_docs.RecyclingList',
        related_name="outfits",
        verbose_name="Ведомость переработки",
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        )
    fuel_distribution = models.ForeignKey(
        'primary_docs.FuelDistribution',
        related_name="outfits",
        verbose_name="Распределение ГСМ",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
        )

    def get_total_fuel(self):
        total_fuel = 0
        for expense in self.expenses.all():
            if expense.material.category.name == 'ГСМ':
                total_fuel += expense.quantity_fact
        return total_fuel

    class Meta:
        verbose_name = 'Наряд-Акт'
        verbose_name_plural = 'Наряд-Акты'

    def __str__(self):
        return 'Наряд-Акт № {}'.format(self.pk)


# Outfit work / Работы для Наряд-Акта

class OutfitWork(models.Model):
    outfit = models.ForeignKey(
            Outfit,
            related_name="works",
            verbose_name="Наряд-акт",
            null=True,
        )
    name = models.CharField('Наименование', max_length=200)
    units = models.ForeignKey(
        Units,
        related_name="outfit_works",
        verbose_name="Еденицы измерения",
        null=True,
        on_delete=models.SET_NULL
        )
    rate = models.DecimalField('Нормы выработки', decimal_places=1, max_digits=8)
    done = models.DecimalField('Выполнено', decimal_places=1, max_digits=8)
    paragraph = models.CharField('Параграф правочника норм', max_length=50)
    done_norms = models.DecimalField('Выполнено норм', decimal_places=2, max_digits=8)
    pricing = models.DecimalField('Расценка, руб.', decimal_places=2, max_digits=8)
    amount = models.DecimalField('Сумма, руб.', decimal_places=2, max_digits=8)
    man_days = models.DecimalField('Человеко-дней.', decimal_places=1, max_digits=8, blank=True)
    auto_days = models.DecimalField('Машино-смен', decimal_places=1, max_digits=8, blank=True, null=True)
    days = models.DecimalField('Количество дней.', max_digits=8, decimal_places=1)

    class Meta:
        verbose_name = 'Работа для наряда'
        verbose_name_plural = 'Работы для наряда'

    def __str__(self):
        return self.name


# Outfit worktime table / Табеля рабочего времени

class OutfitTable(models.Model):
    outfit = models.ForeignKey(
            Outfit,
            related_name="tables",
            verbose_name="Наряд-акт",
            null=True,
        )
    worker = models.ForeignKey(
        Worker, 
        related_name='outfit_tables', 
        verbose_name='Работник',
        null=True,
        on_delete=models.PROTECT
        )
    rank = models.IntegerField('Разряд')
    workdays = JSONField('Рабочие Дни', default={})
    hours = models.IntegerField('Всего часов')
    days = models.DecimalField('Всего дней', decimal_places=1, max_digits=5)
    done = models.DecimalField('Выполнено норм', max_digits=6, decimal_places=2)
    tariff_rate = models.DecimalField(
        'Тарифная ставка',
        decimal_places=2,
        max_digits=10,
    )
    by_coefficient = models.DecimalField(
        'По коэффициенту',
        max_digits=8,
        decimal_places=2,
        blank=True
    )
    by_conditions = models.DecimalField(
        'По условиям труда',
        decimal_places=2,
        max_digits=10,
    )
    importance = models.DecimalField('Ответственные работы', decimal_places=2, max_digits=10, blank=True, null=True)
    bonus = models.DecimalField('Премия', decimal_places=2, max_digits=10, blank=True)
    total = models.DecimalField('Всего', decimal_places=2, max_digits=10)

    class Meta:
        verbose_name = 'Табель'
        verbose_name_plural = 'Табеля'

    def __str__(self):
        return 'Табель расчета для {}'.format(self.worker)

    def workdays_to_json(self):
        return json.dumps(self.workdays)


# Outfit expenses / Расходы материалов для наряд-акта

class OutfitExpense(models.Model):
    outfit = models.ForeignKey(
            Outfit,
            related_name="expenses",
            verbose_name="Наряд-акт",
            null=True,
        )
    material = models.ForeignKey(
            Material,
            related_name="expenses",
            verbose_name="Материал",
            null=True,
            on_delete=models.PROTECT
        )
    quantity_norm = models.DecimalField('Количество по норме', max_digits=8, decimal_places=2)
    quantity_fact = models.DecimalField('Количество по факту', max_digits=8, decimal_places=2)
    cost = models.DecimalField('Стоимость, руб.', decimal_places=2, max_digits=10, blank=True, null=True)

    class Meta:
        verbose_name = 'Расход сырья'
        verbose_name_plural = 'Расходы сырья'   

    def do_expense(self):
        self.material.quantity -= self.quantity_fact
        self.material.save()

    def __str__(self):
        return 'Расход сырья: {} № {}'.format(self.material.name, self.pk)


# On post materials expenses - change material quantity / При создании расходов материалов - изменять их количество

@receiver(models.signals.post_save, sender=OutfitExpense)
def on_create_expense(sender, instance, created, *args, **kwargs):
    if created:
        instance.do_expense()


# Outfits postings / Приходы материалов для наряд-акта

class OutfitPosting(models.Model):
    outfit = models.ForeignKey(
            Outfit,
            related_name="postings",
            verbose_name="Наряд-акт",
            null=True,
        )
    material = models.ForeignKey(
            Material,
            related_name="postings",
            verbose_name="Материал",
            null=True,
            on_delete=models.PROTECT
        )
    quantity = models.DecimalField('Количество', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Приход лесопродукции'
        verbose_name_plural = 'Приходы лесопродукции'

    def do_posting(self):
        self.material.quantity += self.quantity
        self.material.save()

    def __str__(self):
        return 'Приход лесопродукции: {} № {}'.format(self.material.name, self.pk)


# On post materials postings - change material quantity / При приходе материалов - изменить их количество

@receiver(models.signals.post_save, sender=OutfitPosting)
def on_create_posting(sender, instance, created, *args, **kwargs):
    if created:
        instance.do_posting()
        

# Tractor RegForm / Учетный лист тракториста-машиниста

class TractorRegFormWork(models.Model):
    date = models.DateField('Дата')
    event = models.CharField('Наименование', max_length=500, null=True)
    quarter = models.IntegerField('Квартал')
    allotment = models.IntegerField('Выдел')
    area = models.DecimalField('Площадь, расстояние', decimal_places=2, max_digits=10)
    ref_name = models.CharField('Наименование справочника', max_length=50)
    ref_page = models.CharField('Страница справочника', max_length=50)
    units = models.ForeignKey(
        Units,
        related_name="regform_works",
        verbose_name="Еденицы измерения",
        null=True,
        on_delete=models.SET_NULL
        )
    hours = models.DecimalField('Отработано часов', decimal_places=2, max_digits=5)
    rate = models.DecimalField('Норма выработки', decimal_places=2, max_digits=10)
    pricing = models.DecimalField('Расценка', decimal_places=2, max_digits=10)
    complete_nature = models.DecimalField('Выполнено, в натуре', decimal_places=2, max_digits=10)
    complete_norms = models.DecimalField('Выполнено сменных норм', decimal_places=2, max_digits=10)
    amount = models.DecimalField('Оплата: основная', decimal_places=2, max_digits=10)
    bonus = models.DecimalField('Оплата: премия', decimal_places=2, max_digits=10)
    complexity = models.DecimalField('Оплата: сложность', decimal_places=2, max_digits=10)
    classines = models.DecimalField('Оплата: классность', decimal_places=2, max_digits=10)
    amount_total = models.DecimalField('Оплата: всего', decimal_places=2, max_digits=10)
    distance = models.DecimalField('Расстояние', decimal_places=2, max_digits=10, null=True, blank=True)
    fuel_per_unit = models.DecimalField('Расход горючего на еденицу работы', decimal_places=2, max_digits=10)
    fuel = models.DecimalField('Расход горючего всего', decimal_places=2, max_digits=10)

    class Meta:
        verbose_name = 'Работа тракториста-машиниста'
        verbose_name_plural = 'Работы тракториста-машиниста'

    def __str__(self):
        return 'Работа тракториста-машиниста № {}'.format(self.pk)


class TractorRegForm(models.Model):
    date = models.DateField('Дата')
    event = models.ForeignKey(
        OutfitEvent,
        related_name="regforms",
        verbose_name="Мероприятие",
        null=True,
        on_delete=models.PROTECT
        )
    table_number = models.CharField('Табельный номер', max_length=50, blank=True, null=True)
    bonus = models.IntegerField('Премия', blank=True, null=True)
    complexity = models.IntegerField('Сложность', blank=True, null=True)
    importance = models.IntegerField('Ответственные работы', blank=True, null=True)
    classines = models.IntegerField('Классность', blank=True, null=True)
    brigade = models.CharField('Бригада', blank=True, max_length=50, null=True)
    departament = models.CharField(
        'Отдел',
        choices=DEPARTAMENTS,
        max_length=50,
        null=True
        )

    works = models.ManyToManyField(
        TractorRegFormWork,
        related_name='tractor_regform',
        verbose_name="Работы"
        )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="tractor_regforms",
        verbose_name="Автор",
        null=True,
        on_delete=models.SET_NULL
        )
    conducted = models.BooleanField(
        'Проведен',
        default=False
    )
    organization = models.ForeignKey(
        Organization,
        related_name='tractor_regforms',
        verbose_name='Организация',
        null=True,
        on_delete=models.SET_NULL
    )
    driver = models.ForeignKey(
        Worker,
        related_name="tractor_regforms_driver",
        verbose_name="Тракторист",
        null=True,
        on_delete=models.PROTECT
        )
    car = models.ForeignKey(
        Car,
        related_name="tractor_regforms",
        verbose_name="Трактор",
        null=True,
        on_delete=models.PROTECT
        )
    trailerman = models.ForeignKey(
        Worker,
        related_name="tractor_regforms_trailerman",
        verbose_name="Прицепщик",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
        )
    station = models.ForeignKey(
        Station,
        related_name='tractor_regforms',
        verbose_name='Отделение (участок)',
        null=True,
        on_delete=models.PROTECT
        )
    brigadier = models.ForeignKey(
        Worker,
        related_name="tractor_regforms_brigadier",
        verbose_name="Бригадир",
        null=True,
        on_delete=models.PROTECT
        )
    trailer = models.CharField('Прицепное устройство', max_length=50, blank=True, null=True)
    total_hours = models.DecimalField('Отработано часов', decimal_places=2, max_digits=10)
    total_complete_nature = models.DecimalField('Выполнено: в натуре', decimal_places=2, max_digits=10)
    total_complete_norms = models.DecimalField('Выполнено: сменных норм', decimal_places=2, max_digits=10)
    amount = models.DecimalField('Оплата: основная', decimal_places=2, max_digits=10)
    amount_bonus = models.DecimalField('Оплата: премия', decimal_places=2, max_digits=10, null=True, blank=True)
    amount_importance = models.DecimalField('Оплата: ответственные работы', decimal_places=2, max_digits=10, null=True, blank=True)
    amount_complexity = models.DecimalField('Оплата: сложность', decimal_places=2, max_digits=10, null=True, blank=True)
    amount_classines = models.DecimalField('Оплата: классность', decimal_places=2, max_digits=10, null=True, blank=True)
    amount_total = models.DecimalField('Оплата: всего', decimal_places=2, max_digits=10)
    fuel_dep = models.DecimalField('Горючее: остаток при получении учетного листа', decimal_places=2, max_digits=10)
    fuel_issued = models.DecimalField('Горючее: заправлено', decimal_places=2, max_digits=10, null=True, blank=True)
    fuel_ret = models.DecimalField('Горючее: остаток при сдаче учетного листа', decimal_places=2, max_digits=10)
    total_fuel = models.DecimalField('Горючее: расход', decimal_places=2, max_digits=10)

    fuel_distribution = models.ForeignKey(
        'primary_docs.FuelDistribution',
        related_name="regforms",
        verbose_name="Распределение ГСМ",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
        )

    class Meta:
        verbose_name = 'Учетный лист тракториста-машиниста'
        verbose_name_plural = 'Учетные листы тракториста-машиниста'

    def __str__(self):
        return 'Учетный лист № {}'.format(self.pk)


# Statements / Ведомости

class SvodnayaZapis(models.Model):
    # Расчет для сводной ведомости
    waybill = models.ForeignKey(
        Waybill,
        related_name="svodnaya",
        verbose_name="Путевой лист",
        null=True,
        on_delete=models.PROTECT
        )
    rate = models.DecimalField('Ставка', decimal_places=2, max_digits=10)
    bonus = models.DecimalField('Премия', decimal_places=2, max_digits=10, blank=True, null=True)
    coefficient = models.DecimalField('Коэффициент', decimal_places=2, max_digits=10, blank=True, null=True)
    classines = models.DecimalField('Классность', decimal_places=2, max_digits=10, blank=True, null=True)
    amount = models.DecimalField('Оплата: основная', decimal_places=2, max_digits=10)
    amount_classines = models.DecimalField('Оплата: классность', decimal_places=2, max_digits=10, blank=True, null=True)
    recast_half = models.DecimalField('Оплата: переработка в 1,5 раз', decimal_places=2, max_digits=10, blank=True, null=True)
    recast_double = models.DecimalField('Оплата: переработка в 2 раза', decimal_places=2, max_digits=10, blank=True, null=True)
    amount_holydays = models.DecimalField('Оплата: празднечные', decimal_places=2, max_digits=10, blank=True, null=True)
    amount_bonus = models.DecimalField('Оплата: премия', decimal_places=2, max_digits=10, blank=True, null=True)
    amount_coefficient = models.DecimalField('Оплата: коэффициент', decimal_places=2, max_digits=10, blank=True, null=True)
    amount_total = models.DecimalField('Оплата: всего', decimal_places=2, max_digits=10)

    class Meta:
        verbose_name = 'Сводный расчет'
        verbose_name_plural = 'Сводные расчеты'

    def __str__(self):
        return 'Сводный расчет № {}'.format(self.pk)


class Vedomost(models.Model):
    # Базовый класс для ведомостей
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Составитель",
        null=True,
        on_delete=models.SET_NULL
        )
    station = models.ForeignKey(
        Station,
        verbose_name="Производственный участок",
        null=True,
        on_delete=models.PROTECT
        )
    departament = models.CharField(
        'Отдел',
        choices=DEPARTAMENTS,
        max_length=50,
        null=True
        )
    conducted = models.BooleanField(
        'Проведен',
        default=False
    )
    date = models.DateField('Дата')
    created_date = models.DateField('Дата составления', default=timezone.now)
    event = models.ForeignKey(
            OutfitEvent,
            verbose_name="Вид работ",
            blank=True,
            null=True,
            on_delete=models.PROTECT
        )

    # Total data / Суммарные данные
    amount = models.DecimalField('Оплата: основная', decimal_places=2, max_digits=10, null=True)
    complexity = models.DecimalField('Оплата: сложность (условия труда)', decimal_places=2, max_digits=10, blank=True, null=True)
    classines = models.DecimalField('Оплата: классность', decimal_places=2, max_digits=10, blank=True, null=True)
    importance = models.DecimalField('Оплата: ответственные работы', decimal_places=2, max_digits=10, blank=True, null=True)
    recast_half = models.DecimalField('Оплата: переработка в 1,5 раз', decimal_places=2, max_digits=10, blank=True, null=True)
    recast_double = models.DecimalField('Оплата: переработка в 2 раза', decimal_places=2, max_digits=10, blank=True, null=True)
    holydays = models.DecimalField('Оплата: выходные', decimal_places=2, max_digits=10, blank=True, null=True)
    bonus = models.DecimalField('Оплата: премия', decimal_places=2, max_digits=10, blank=True, null=True)
    coefficient = models.DecimalField('Оплата: коэффициент', decimal_places=2, max_digits=10, blank=True, null=True)
    amount_total = models.DecimalField('Оплата: всего', decimal_places=2, max_digits=10)

    class Meta:
        abstract = True
    

class SvodnayaVedomost(Vedomost):
    # Сводная ведомость по начислению зароботной платы водителям
    hours = models.DecimalField('Часы', decimal_places=2, max_digits=10)
    calcs = models.ManyToManyField(
        SvodnayaZapis,
        related_name="svodnaya_vedomost",
        verbose_name="Сводные расчеты"
        )

    class Meta:
        default_related_name = 'svodnaya_vedomost'
        verbose_name = 'Сводная ведомость'
        verbose_name_plural = 'Сводные ведомости'

    def __str__(self):
        return 'Сводная ведомость № {}'.format(self.pk)


class NakopitelnayaVedomost(Vedomost):
    # Накопительная ведомость по зароботной плате

    man_days = models.DecimalField(
        'Человеко-дней(машино-смен)',
        decimal_places=2, max_digits=10
        )
    outfits = models.ManyToManyField(
        Outfit,
        related_name='vedomost',
        verbose_name='Наряд-Акты',
        blank=True
        )
    regforms = models.ManyToManyField(
        TractorRegForm,
        related_name="vedomost",
        verbose_name="Учетные листы тракториста-машиниста",
        blank=True
        )

    class Meta:
        default_related_name = 'nakopitelnaya_vedomost'
        verbose_name = 'Накопительная ведомость'
        verbose_name_plural = 'Накопительные ведомости'

    def __str__(self):
        return 'Накопительная ведомость № {}'.format(self.pk)

    def get_calcs_counter(self):
        regforms = self.outfits.count()
        outfits = 0
        for of in self.outfits.all():
            outfits += of.tables.count()
        return regforms + outfits


# Tables of worktime / Табель учета рабочего времени

class WorkTimeEntry(models.Model):
    worker = models.ForeignKey(
        Worker,
        related_name="worktime_entries",
        verbose_name="Записи учета времени",
        on_delete=models.PROTECT
        )
    workdays = JSONField('Рабочие Дни', default={})

    class Meta:
        verbose_name = 'Запись табеля учета рабочего времени'
        verbose_name_plural = 'Записи табеля учета рабочего времени'

    def __str__(self):
        return 'Запись учета рабочего времени для {}'.format(self.worker.get_full_name)


class WorkTimeTable(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Составитель",
        related_name="worktime_tables",
        null=True,
        on_delete=models.SET_NULL
        )
    date = models.DateField('Период')
    hours = models.DecimalField('Всего часов', null=True, decimal_places=2, max_digits=10)
    created_date = models.DateTimeField('Дата создания', default=timezone.now)
    organization = models.ForeignKey(
        Organization,
        related_name="worktime_tables",
        verbose_name="Организация",
        null=True,
        on_delete=models.PROTECT,
        default=1
        )
    station = models.ForeignKey(
        Station,
        related_name="worktime_tables",
        verbose_name="Участок",
        null=True,
        on_delete=models.PROTECT
        )
    departament = models.CharField(
        'Отдел',
        choices=DEPARTAMENTS,
        max_length=50,
        null=True
        )
    responsible = models.ForeignKey(
        Worker,
        related_name="worktime_tables_responsible",
        verbose_name="Ответственный",
        null=True,
        on_delete=models.PROTECT
        )
    performer = models.ForeignKey(
        Worker,
        related_name="worktime_tables_performer",
        verbose_name="Исполнитель",
        null=True,
        on_delete=models.PROTECT
        )
    outfits = models.ManyToManyField(
        Outfit,
        related_name="worktime_table",
        verbose_name="Наряд-Акты",
        blank=True
        )
    regforms = models.ManyToManyField(
        TractorRegForm,
        related_name="worktime_table",
        verbose_name="Учетные листы тракториста-машиниста",
        blank=True
        )
    waybills = models.ManyToManyField(
        Waybill,
        related_name="worktime_table",
        verbose_name="Путевые листы",
        blank=True
        )
    entries = models.ManyToManyField(
        WorkTimeEntry,
        related_name="worktime_table",
        verbose_name="Записи",
        blank=True
        )

    class Meta:
        verbose_name = 'Табель учета рабочего времени'
        verbose_name_plural = 'Табеля учета рабочего времени'

    def __str__(self):
        return 'Табель учета рабочего времени № {}'.format(self.pk)

    def get_calcs(self):
        workers = set()
        tables = []
        calcs = []
        for outfit in self.outfits.all():
            for table in outfit.tables.all():
                workers.add(table.worker)
                tables.append(table)
        for worker in workers:
            worker_calcs = list(filter(lambda x: x.worker.pk == worker.pk, tables))
            workdays = {}
            wd = list(map(lambda x: x.workdays, worker_calcs))
            for d in wd:
                for k in d.keys():
                    workdays[k] = workdays.get(k,0) + d[k]
            calc = dict(
                worker=worker,
                workdays=workdays
                )
            calcs.append(calc)
        return calcs


# Acceptance report forest products / Акт прихода лесопродукции
class ForestArrivalReport(models.Model):
    station = models.ForeignKey(
        Station,
        related_name="forest_arrival_reports",
        verbose_name="Участок",
        null=True,
        on_delete=models.PROTECT
        )
    date = models.DateTimeField('Дата', null=True)
    created_date = models.DateTimeField('Дата создания', default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="forest_arrival_reports",
        verbose_name="Составитель",
        null=True,
        on_delete=models.SET_NULL
        )
    postings = models.ManyToManyField(
        OutfitPosting,
        related_name="forest_arrival_reports",
        verbose_name="Приход лесопродукции",
        blank=True
        )

    class Meta:
        verbose_name = 'Акт прихода лесопродукции'
        verbose_name_plural = 'Акты прихода лесопродукции'

    def __str__(self):
        return 'Акт прихода лесопродукции № {}'.format(self.pk)


# Recycling list / Ведомость переработки

class RecyclingList(models.Model):
    station = models.ForeignKey(
        Station,
        related_name="recycling_lists",
        verbose_name="Участок",
        null=True,
        on_delete=models.PROTECT
        )
    date = models.DateTimeField('Дата', null=True)
    created_date = models.DateTimeField('Дата создания', default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="recycling_lists",
        verbose_name="Составитель",
        null=True,
        on_delete=models.SET_NULL
        )

    class Meta:
            verbose_name = 'Ведомость переработки'
            verbose_name_plural = 'Ведомости переработки'

    def __str__(self):
        return 'Ведомость переработки № {}'.format(self.pk)


# Handout / Раздаточная ведомость

class Handout(models.Model):
    station = models.ForeignKey(
        Station,
        related_name="handouts",
        verbose_name="Участок",
        null=True,
        on_delete=models.PROTECT
        )
    car = models.ForeignKey(
        Car,
        related_name="handouts",
        verbose_name="Автомобиль",
        null=True,
        on_delete=models.PROTECT
        )
    worker = models.ForeignKey(
        Worker,
        related_name="handouts",
        verbose_name="Водитель",
        null=True,
        on_delete=models.PROTECT
        )
    date = models.DateTimeField('Дата', null=True)
    created_date = models.DateTimeField('Дата создания', default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="handouts",
        verbose_name="Составитель",
        null=True,
        on_delete=models.SET_NULL
        )

    class Meta:
            verbose_name = 'Раздаточная ведомость'
            verbose_name_plural = 'Раздаточные ведомости'

    def __str__(self):
        return 'Раздаточная ведомость № {}'.format(self.pk)


# Fuel distribution / Распределение ГСМ

class FuelDistribution(models.Model):
    station = models.ForeignKey(
        Station,
        related_name="fuel_distributions",
        verbose_name="Участок",
        null=True,
        on_delete=models.PROTECT
        )
    worker = models.ForeignKey(
        Worker,
        related_name="fuel_distributions",
        verbose_name="Работник",
        null=True,
        on_delete=models.PROTECT
        )
    car = models.ForeignKey(
        Car,
        related_name="fuel_distributions",
        verbose_name="Автомобиль",
        null=True,
        blank=True,
        on_delete=models.PROTECT
        )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="fuel_distributions",
        verbose_name="Составитель",
        null=True,
        on_delete=models.SET_NULL
        )
    total_fuel = models.DecimalField('Всего ГСМ', max_digits=10, decimal_places=2, null=True)
    date = models.DateTimeField('Дата', null=True)
    created_date = models.DateTimeField('Дата создания', default=timezone.now)
    kind = models.CharField(
        'Тип документа',
        choices=CHOICES_OF_FUEL_DISTRIBUTION,
        max_length=50,
        null=True
        )

    class Meta:
        verbose_name = 'Распределение ГСМ'
        verbose_name_plural = 'Распределения ГСМ'

    def __str__(self):
        return 'Распределение ГСМ № {}'.format(self.pk)


# Act of writen / Акт списания материальных запасов

class ActSpisanya(models.Model):
    organization = models.ForeignKey(
        Organization,
        related_name="act_spisanya",
        verbose_name="Организация",
        null=True,
        on_delete=models.PROTECT
        )
    station = models.ForeignKey(
        Station,
        related_name="act_spisanya",
        verbose_name="Участок",
        null=True,
        on_delete=models.PROTECT
        )
    outfit = models.OneToOneField(
        Outfit,
        related_name="act_spisanya",
        verbose_name="Наряд-акт",
        null=True,
        on_delete=models.PROTECT
        )
    comission = models.ManyToManyField(
        Worker,
        related_name="act_spisanya",
        verbose_name="Комиссия",
        )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="act_spisanya",
        verbose_name="Составитель",
        null=True,
        on_delete=models.SET_NULL
        )
    date = models.DateTimeField('Дата', null=True)
    created_date = models.DateTimeField('Дата создания', default=timezone.now)
    order = models.CharField('Распоряжение', null=True, max_length=50)

    class Meta:
        verbose_name = 'Акт списания материальных запасов'
        verbose_name_plural = 'Акты списания материальных запасов'

    def __str__(self):
        return 'Акт списания материальных запасов № {}'.format(self.pk)