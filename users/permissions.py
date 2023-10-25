from rest_framework.permissions import BasePermission


class IsModeratorBanLesson(BasePermission):
    """
    Запрет модераторам для создания/удаления уроков.
    """
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Модераторы').exists():
            return request.method in ['GET', 'HEAD', 'PUT']
        return True


class IsOwnerOfStaff(BasePermission):
    """
    Проверяет, является ли текущий пользователь владельцем объекта или персоналом.
    """
    def has_permission(self, request, view):
        user = request.user

        return view.queryset.filter(owner=user).exists() or user.is_staff


class IsModeratorReadOnlyUpdate(BasePermission):
    """
    Запрет модераторам на создание/удаление курса.
    """
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Модераторы').exists():
            return request.method in ['GET', 'HEAD', 'PUT']
        return True
