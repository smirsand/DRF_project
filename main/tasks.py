from datetime import datetime, timedelta

from celery import shared_task
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail

from .models import Course


@shared_task
def send_course_update_emails(course_id):
    """
    Отправляет электронное письмо клиенту после обновления курса.
    """

    course = Course.objects.get(id=course_id)
    send_mail(
        subject=f'Обновление курса',
        message=f'Курс {course.name_course} был обновлен. Проверьте новые материалы!',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email for user in User.objects.all()],  # получатели писем,
    )


def user_blocking_task():
    """
    Блокирует пользователя если он не был активен 30 дней.
    """

    users_list = User.objects.all()
    today = datetime.utcnow()
    threshold = today - timedelta(days=30)

    for user in users_list:
        if user.is_active and user.last_login <= threshold:
            user.is_active = False
            user.save()
