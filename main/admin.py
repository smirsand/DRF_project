from django.contrib import admin

from main.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name_course', 'preview_course', 'description_course')
    verbose_name = 'Курс'
    verbose_name_plural = 'Курсы'


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name_lesson', 'description_lesson', 'preview_lesson', 'video_link_lesson')
    verbose_name = 'Урок'
    verbose_name_plural = 'Уроки'
