from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from main.models import Course, Lesson, Payment
from main.serliazers import CourseSerializer, LessonSerializer, PaymentSerializer
from users.permissions import IsModeratorBan, IsModeratorOrReadUpdateOnly


class CourseViewSet(viewsets.ModelViewSet):
    """
    Контроллер ViewSet модели Курс.
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsModeratorOrReadUpdateOnly]


# -------------------------------------------------------------------------------


class LessonCreateAPIView(generics.CreateAPIView):
    """
    Контроллер создания урока
    """
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModeratorBan]


class LessonListAPIView(generics.ListAPIView):
    """
    Контроллер списка уроков
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """
    Контроллер просмотра одного урока
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """
    Контроллер редактирования урока
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """
    Контроллер удаления урока
    """
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModeratorBan]


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

