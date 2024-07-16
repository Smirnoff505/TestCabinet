import random

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя"""
    username = models.IntegerField(null=True, blank=True, unique=True, verbose_name='Логин')
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=150, null=True, blank=True, verbose_name='Отчество')
    phone = models.CharField(max_length=35, unique=True, verbose_name='Телефон')
    email = models.EmailField(unique=True, verbose_name='Почта')
    create_user = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_user = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_active = models.BooleanField(default=True, verbose_name='Активный')

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
