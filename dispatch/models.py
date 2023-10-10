from django.db import models

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
    time = models.DateTimeField(verbose_name='время рассылки')
    frequency = models.CharField(max_length=50, choices=time_mode, verbose_name='периодичность рассылки')
    status = models.CharField(max_length=150, choices=status_mode, verbose_name='статус рассылки')
    clients = models.ManyToManyField(Client, related_name='dispatches', verbose_name='рассылки клиентов')

    def __str__(self):
        return f'{self.time}:{self.frequency} | {self.status}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class Message(models.Model):
    title = models.CharField(max_length=150, verbose_name='тема письма')
    message = models.CharField(max_length=150, verbose_name='текст письма')
    dispatch = models.ForeignKey(Dispatch, on_delete=models.CASCADE, related_name='messages', verbose_name='сообщения рассылки')

    def __str__(self):
        return f'{self.title}: {self.message} | {self.dispatch}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Logs(models.Model):
    last_attempt = models.DateTimeField(verbose_name='дата и время последней попытки')
    status = models.BooleanField(verbose_name='статус попытки')
    server_response = models.TextField(verbose_name='ответ почтового сервера')
    dispatch = models.ForeignKey(Dispatch, on_delete=models.CASCADE, related_name='logs', verbose_name='логи рассылки')

    def __str__(self):
        return f'{self.last_attempt}: {self.status}'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'

