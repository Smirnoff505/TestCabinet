from django.db import models

from config import settings
from users.models import User


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Статья')
    content = models.TextField(verbose_name='Контент')
    create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    picture = models.ImageField(null=True, blank=True, verbose_name='Изображение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
        ordering = ['-create']


class Contract(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', related_name='contract')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'
