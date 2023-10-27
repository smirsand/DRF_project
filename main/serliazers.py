from rest_framework import serializers

from main.models import Course, Lesson, Payment, Subscription
from main.validators import VideoLinkLessonValidator


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [VideoLinkLessonValidator(field='video_link_lesson')]


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)
    subscribed = serializers.SerializerMethodField()

    def get_subscribed(self, obj):
        request = self.context.get('request')
        user = request.user

        if not user.is_authenticated:
            return False

        subscription = Subscription.objects.filter(course=obj, user=user).exists()
        return subscription

    def get_lessons_count(self, obj):
        return obj.lesson_set.count()

    class Meta:
        model = Course
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
