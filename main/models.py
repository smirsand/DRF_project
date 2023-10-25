from django.conf import settings
from django.db import models

from users.models import User


class Course(models.Model):
    """
    Модель курса.
    """

    name_course = models.CharField(max_length=255, verbose_name='название', blank=True, null=True)
    preview_course = models.ImageField(upload_to='course_previews/', verbose_name='превью', blank=True, null=True)
    description_course = models.TextField(verbose_name='описание', blank=True, null=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name_course if self.name_course else "Unnamed course"

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    """
    Модель урока.
    """

    name_lesson = models.CharField(max_length=255, verbose_name='название', blank=True, null=True)
    description_lesson = models.TextField(verbose_name='описание', blank=True, null=True)
    preview_lesson = models.ImageField(upload_to='lesson_previews/', verbose_name='превью', blank=True, null=True)
    video_link_lesson = models.URLField(verbose_name='ссылка на видео', blank=True, null=True)

    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None, verbose_name='курс')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name_lesson if self.name_lesson else "Unnamed Lesson"

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Payment(models.Model):
    """
    Модель платежа.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', blank=True, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='урок', blank=True, null=True)
    payment_date = models.DateField(verbose_name='дата оплаты', auto_now_add=True)
    amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(choices=[('cash', 'Наличные'), ('transfer', 'Перевод на счет')],
                                      verbose_name='способ оплаты')

    def __str__(self):
        return f'Платеж {self.id}, {self.user} от {self.payment_date}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
