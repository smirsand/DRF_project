from rest_framework.permissions import BasePermission


class IsModeratorBan(BasePermission):
    """
    Запрет модераторам.
    """
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Модераторы').exists():
            return False
        return True


class IsModeratorOrReadUpdateOnly(BasePermission):
    """
    Запрет модераторам на создание/удаление курса и урока.
    """
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Модераторы').exists():
            return request.method in ['GET', 'HEAD', 'PUT', 'PATCH']
        return False
