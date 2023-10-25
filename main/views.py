from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from main.models import Course, Lesson, Payment
from main.serliazers import CourseSerializer, LessonSerializer, PaymentSerializer
from users.permissions import IsModeratorBanLesson, IsOwnerOfStaff, IsModeratorReadOnlyUpdate


class CourseViewSet(viewsets.ModelViewSet):
    """
    Контроллер ViewSet модели Курс.
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsModeratorReadOnlyUpdate, IsOwnerOfStaff]

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Модераторы').exists():
            return Course.objects.all()
        else:
            return Course.objects.filter(owner=user)


# -------------------------------------------------------------------------------


class LessonCreateAPIView(generics.CreateAPIView):
    """
    Контроллер создания урока
    """
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModeratorBanLesson]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    """
    Контроллер списка уроков
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModeratorBanLesson]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Модераторы').exists():
            return Lesson.objects.all()
        else:
            return Lesson.objects.filter(owner=user)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """
    Контроллер просмотра одного урока
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModeratorBanLesson, IsOwnerOfStaff]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """
    Контроллер редактирования урока
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModeratorBanLesson, IsOwnerOfStaff]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """
    Контроллер удаления урока
    """
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModeratorBanLesson, IsOwnerOfStaff]


# --------------------------------------------------------------------------------


class PaymentCreateAPIView(generics.CreateAPIView):
    """
    Контроллер создания платежа
    """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]


class PaymentListAPIView(generics.ListAPIView):
    """
    Контроллер списка платежей
    """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('payment_date', 'payment_method', 'course')  # Набор полей для фильтрации
    ordering_fields = ['payment_date', 'payment_method']  # Набор полей для фильтрации
    permission_classes = [IsAuthenticated]
