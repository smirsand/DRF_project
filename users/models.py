from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
        Модель пользователя.
        """
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=35, verbose_name='телефон', blank=True, null=True)
    city = models.CharField(max_length=100, verbose_name='город', blank=True, null=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
