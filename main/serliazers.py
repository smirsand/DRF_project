from rest_framework import serializers

from main.models import Course, Lesson, Payment


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    # получение количества уроков.
    def get_lessons_count(self, obj):
        return obj.lesson_set.count()

    class Meta:
        model = Course
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
