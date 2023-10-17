from django.db import models


class Course(models.Model):
    """
    Модель курса.
    """
    name = models.CharField(max_length=255, verbose_name='название')
    preview = models.ImageField(upload_to='course_previews/', verbose_name='превью', blank=True, null=True)
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='lesson_previews/', verbose_name='превью', blank=True, null=True)
    video_link = models.URLField(verbose_name='ссылка на видео', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
