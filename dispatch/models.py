from django.contrib.auth import get_user
from django.core import serializers

from django.db import models

from users.models import User

NULLABLE = {"null": True, "blank": True}


class Client(models.Model):
    email = models.EmailField(verbose_name='почта')
    name = models.CharField(max_length=150, verbose_name='имя')
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.name}: {self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ('name',)


class Dispatch(models.Model):
    time_mode = [
        ('раз в день', 'Раз в день'),
        ('раз в неделю', 'Раз в неделю'),
        ('раз в месяц', 'Раз в месяц'),
    ]
    status_mode = [
        ('завершена', 'Завершена'),
        ('создана', 'Создана'),
        ('запущена', 'Запущена'),
    ]
    start_time = models.DateTimeField(verbose_name='время начала рассылки')
    end_time = models.DateTimeField(verbose_name='время окончания рассылки')
    frequency = models.CharField(max_length=50, choices=time_mode, verbose_name='периодичность рассылки')
    status = models.CharField(max_length=150, choices=status_mode, verbose_name='статус рассылки')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='dispatches',
                               verbose_name='рассылки клиента')
    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)


    def __str__(self):
        return f'Клиент: {self.client}\n ' \
               f'Время начала рассылки: {self.start_time}\n' \
               f'Время окончания рассылки: {self.end_time}\n' \
               f'Частота рассылки: {self.frequency}\n' \
               f'Статус рассылки: {self.status}\n'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class Message(models.Model):
    title = models.CharField(max_length=150, verbose_name='тема письма')
    message = models.CharField(max_length=150, verbose_name='текст письма')
    dispatch = models.ForeignKey(Dispatch, on_delete=models.CASCADE,
                                 related_name='messages', verbose_name='выбрать рассылку', **NULLABLE)

    def __str__(self):
        return f'{self.title}: {self.message} | {self.dispatch}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Logs(models.Model):
    last_attempt = models.DateTimeField(verbose_name='дата и время последней попытки')
    status = models.CharField(max_length=20, verbose_name='статус попытки')
    server_response = models.TextField(verbose_name='ответ почтового сервера', **NULLABLE)
    dispatch = models.ForeignKey(Dispatch, on_delete=models.CASCADE, related_name='logs',
                                 verbose_name='логи рассылки', **NULLABLE)

    def __str__(self):
        return f'{self.last_attempt}: {self.status}'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'

