from django.db import models
from django.utils.timezone import now


NULLABLE = {"null": True, "blank": True}

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(default='', max_length=100, verbose_name='slug')
    content = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='blog_images/', verbose_name='изображение', **NULLABLE)
    created_date = models.DateField(verbose_name='дата создания', default=now)
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
