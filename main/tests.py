from rest_framework import status
from rest_framework.test import APITestCase

from main.models import Lesson, Course
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.course = Course.objects.create(name_course="Курс 1")

        self.user = User.objects.create(email='test@mail.ru', password='test', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=self.user)

        self.lesson = Lesson.objects.create(name_lesson="Урок 1", course=self.course)
        self.lesson.owner = self.user
        self.lesson.save()

    def test_create_lesson(self):
        """
        Тест создания урока.
        """
        data = {
            "course": self.course.id
        }

        response = self.client.post('/lesson/create/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)
        self.assertEqual(response.data['course'], self.course.id)

        self.assertEqual(
            response.json(),
            {
                "id": 2,
                "name_lesson": None,
                "description_lesson": None,
                "preview_lesson": None,
                "video_link_lesson": None,
                "course": 1,
                "owner": 1
            }
        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )
