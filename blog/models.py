from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    title = models.CharField('Название поста', max_length=200)
    annotation = models.TextField('Краткий текст')
    body = models.TextField('Полный текст')
    created_at = models.DateTimeField('Дата создания',
                                      default=timezone.now())
    published = models.BooleanField('Опубликовано', default=False)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title