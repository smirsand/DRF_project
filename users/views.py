from rest_framework import viewsets

from users.models import User
from users.serliazers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Контроллер ViewSet модели Пользователь.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
