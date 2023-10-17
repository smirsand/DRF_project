from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Класс нового пользователя.
    """

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='smirsand@mail.ru',
            first_name='Сергей',
            last_name='Смирнов',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('2721896')
        user.save()