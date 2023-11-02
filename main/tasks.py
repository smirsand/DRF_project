from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from users.models import User
from .models import Course


@shared_task
def send_course_update_emails(course_id, *args, **kwargs):
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
