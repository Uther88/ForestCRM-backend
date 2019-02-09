from datetime import datetime
import os

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, AbstractBaseUser
from django.utils import timezone



from primary_docs.models import Organization, Station


# Path for save files / Путь сохранения файлов
def upload_file(instance, filename):
    return 'files/{0}/{1}'.format(instance.sender.username, filename)


# Important values for tasks / Уровни важности заданий
R = 'danger'
Y = 'warning'
G = 'success'

IMPORTANCE = (
    (R, 'высокая'),
    (Y, 'средняя'),
    (G, 'низкая')
)


# Custom user model / Измененная модель пользователя
class User(AbstractUser):
    third_name = models.CharField('Отчество', max_length=50)
    position = models.CharField('Должность', max_length=50)
    organization = models.ForeignKey(
        Organization, 
        on_delete=models.SET_NULL, 
        verbose_name='Организация',
        related_name='employees', 
        blank=True, null=True
    )
    station = models.ForeignKey(
        Station, 
        on_delete=models.SET_NULL, 
        verbose_name='Участок',
        related_name='employees', 
        blank=True, null=True
    )
    avatar = models.ImageField(
        verbose_name='Аватар',
        max_length=255, 
        upload_to='images/avatars/', 
        blank=True
    )

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def get_full_name(self):
        return '{0} {1}. {2}.'.format(self.last_name, self.first_name[0], self.third_name[0])

    def __str__(self):
        if self.last_name and self.first_name and self.third_name:
            return self.get_full_name()
        return self.username


# Bug report model
class BugReport(models.Model):
    reporter = models.ForeignKey('User', related_name="reports", verbose_name="Отправитель")
    text = models.TextField('Описание', max_length=500)

    class Meta:
        verbose_name = 'Отчет об ошибке'
        verbose_name_plural = 'Отчеты об ошибках'

    def __str__(self):
        return 'Отчет № {}'.format(self.id)


# File model / Модель файла
class File(models.Model):
    title = models.CharField('Название', max_length=50, default=None)
    description = models.TextField(
        'Описание', max_length=255, blank=True, default=None, null=True)
    recipient = models.ManyToManyField(
        User, verbose_name='Получатель', related_name='received_files', blank=True)
    sender = models.ForeignKey(
        User, verbose_name='Отправитель', related_name='send_files', null=True, blank=True)
    file = models.FileField('Файл', max_length=255, upload_to=upload_file)

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def __str__(self):
        return os.path.basename(self.file.name)

    def terminate(self):
        if os.path.exists(self.file.path):
            os.remove(self.file.path)
        self.delete()


@receiver(pre_delete, sender=File)
def delete_file(sender, instance, **kwargs):
    instance.file.delete(False)


# Task model / Модель заданий
class Task(models.Model):
    performer = models.ForeignKey(
        User, 
        verbose_name='Исполнитель', 
        related_name='tasks', 
        null=True, 
        default=User
        )
    assigner = models.ForeignKey(
        User, 
        verbose_name='Назначающий', 
        related_name='given_tasks', 
        null=True
        )

    importance = models.CharField(
        'Важность', 
        null=True, 
        choices=IMPORTANCE, 
        max_length=10
        )
    files = models.ManyToManyField(
        File, 
        verbose_name='Файлы', 
        related_name='task', 
        max_length=255, 
        blank=True
        )
    title = models.CharField('Название', max_length=50, default=None)
    text = models.TextField(
        'Описание', 
        max_length=350, 
        default=None, 
        null=True
        )
    created_date = models.DateTimeField('Созданно', default=timezone.now)
    completed_date = models.DateTimeField(
        'Выполнено', 
        default=None, 
        blank=True, 
        null=True
        )
    to_complete = models.DateTimeField(
        'Выполнить до', 
        default=None
        )
    is_completed = models.BooleanField('Завершено', default=False)
    viewed = models.BooleanField('Просмотренно', default=False)
    comment = models.TextField(
        'Комментарий', 
        max_length=500, 
        null=True, 
        blank=True
        )

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        ordering = ['-to_complete']

    def __str__(self):
        return self.title

    def complete(self):
        self.is_completed = True
        self.completed_date = timezone.now()
        self.save()

    def get_status(self):
        if not self.is_completed:
            if self.to_complete > timezone.now():
                return 'in_process'
            else:
                return 'overdue'
        else:
            return 'completed'

    def get_style(self):
        if self.is_completed:
            return 'success'
        else:
            return 'danger'


# Message model / Модель сообщений
class Message(models.Model):
    title = models.CharField(verbose_name='Тема', max_length=50, default='Новое сообщение')
    text = models.TextField(verbose_name='Текст', max_length=500, default=None)

    files = models.ManyToManyField(
        File,
        verbose_name='Файлы',
        related_name='messages',
        blank=True
    )
    recipient = models.ManyToManyField(
        User, verbose_name='Кому', related_name='incoming_messages')
    sender = models.ForeignKey(
        User,
        verbose_name='Отправитель',
        related_name='outcoming_messages',
        null=True
    )
    created_date = models.DateTimeField('Созданно', default=timezone.now)
    is_new = models.BooleanField(verbose_name="Не прочитанное", default=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-created_date']

    def __str__(self):
        return self.title

    def read(self):
        self.is_new = False
        self.save()

    def full_delete(self):
        for file in self.files.all():
            file.terminate()
        self.delete()


class Chat(models.Model):
    members = models.ManyToManyField(User, verbose_name="Участники", related_name="chats")
    messages = models.ManyToManyField(Message, verbose_name="Сообщения", related_name="chats")
    updated = models.DateTimeField(null=True)

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
        ordering = ['-updated']
