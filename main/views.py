from rest_framework import viewsets, generics

from main.models import Course, Lesson
from main.serliazers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    Контроллер ViewSet модели Курс.
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


# -------------------------------------------------------------------------------


class LessonCreateAPIView(generics.CreateAPIView):
    """
    Контроллер создания урока
    """
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    """
    Контроллер списка уроков
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """
    Контроллер просмотра одного урока
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    """
    Контроллер редактирования урока
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    """
    Контроллер удаления урока
    """
    queryset = Lesson.objects.all()
