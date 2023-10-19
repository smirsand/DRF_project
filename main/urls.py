from django.urls import path

from main.apps import MainConfig
from rest_framework.routers import DefaultRouter

from main.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, PaymentCreateAPIView, PaymentListAPIView

app_name = MainConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
                  path('lesson/list/', LessonListAPIView.as_view(), name='lesson-list'),
                  path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-retrieve'),
                  path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
                  path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),

                  path('payment/create/', PaymentCreateAPIView.as_view(), name='payment-create'),
                  path('payment/list/', PaymentListAPIView.as_view(), name='payment-list')

              ] + router.urls
