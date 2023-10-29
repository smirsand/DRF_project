from rest_framework import status
from rest_framework.test import APITestCase

from main.models import Lesson, Course, Subscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        # Создание объекта курс.
        self.course = Course.objects.create(name_course="Курс")

        # Создаем пользователя
        self.user = User.objects.create(email='test@mail.ru', password='test', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=self.user)  # Аутентификация пользователя

    def test_create_lesson(self):
        """
        Тест создания урока.
        """
        data = {
            "name_lesson": "Тест",
            "description_lesson": "тест",
            "course": self.course.id
        }

        response = self.client.post(
            '/lesson/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {"id": 1,
             "name_lesson": "Тест",
             "description_lesson": "тест",
             "preview_lesson": None,
             "video_link_lesson": None,
             "course": 1,
             "owner": 1
             }
        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_list_lesson(self):
        """
        Тест списка уроков.
        """

        data = {
            "name_lesson": "Тест",
            "description_lesson": "тест",
            "course": self.course.id
        }

        res = self.client.post(
            '/lesson/create/',
            data=data
        )

        response = self.client.get('/lesson/list/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(response.json(), {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 3,
                    "name_lesson": "Тест",
                    "description_lesson": "тест",
                    "preview_lesson": None,
                    "video_link_lesson": None,
                    "course": 3,
                    "owner": 3
                }
            ]
        }
                         )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_retrieve_lesson(self):
        """
        Тест на просмотр урока.
        """
        data = {
            "name_lesson": "Тест",
            "description_lesson": "тест",
            "course": self.course.id
        }

        res = self.client.post(
            '/lesson/create/',
            data=data, id=1
        )

        lesson_id = res.data['id']

        response = self.client.get(f'/lesson/{lesson_id}/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(response.json(),
                         {'id': 4,
                          'name_lesson': 'Тест',
                          'description_lesson': 'тест',
                          'preview_lesson': None,
                          'video_link_lesson': None,
                          'course': 4,
                          'owner': 4
                          }
                         )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_update_lesson(self):
        """
        Тест на редактирование урока.
        """
        data = {
            "name_lesson": "Тест",
            "description_lesson": "тест",
            "course": self.course.id
        }

        res = self.client.post('/lesson/create/', data=data)
        lesson_id = res.data['id']

        data_update = {
            "name_lesson": "Тест_1",
            "description_lesson": "тест",
            "course": self.course.id
        }

        response = self.client.patch(f'/lesson/update/{lesson_id}/', data=data_update)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertTrue(Lesson.objects.all().exists())

    def test_delete_lesson(self):
        """
        Тест на удаление урока.
        """
        data = {
            "name_lesson": "Тест",
            "description_lesson": "тест",
            "course": self.course.id
        }

        res = self.client.post('/lesson/create/', data=data)
        lesson_id = res.data['id']

        self.assertEqual(
            res.status_code,
            status.HTTP_201_CREATED
        )

        response = self.client.delete(f'/lesson/delete/{lesson_id}/')

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(Lesson.objects.all().exists())


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        # Создание объекта курс.
        self.course = Course.objects.create(name_course="Курс")

        # Создаем пользователя
        self.user = User.objects.create(email='test@mail.ru', password='test', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=self.user)  # Аутентификация пользователя

    def test_create_subscription(self):
        """
        Тест на создание обновления курса.
        """
        data = {"course": self.course.pk, "subscription": True, "user": self.user.pk}

        response = self.client.post('/subscription/create/', data=data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        self.assertEquals(response.json(), {
            "id": 1,
            "subscription": True,
            "course": self.course.pk,
            "user": self.user.pk
        })

        self.assertTrue(Subscription.objects.all().exists())

    def test_delete_subscription(self):
        """
        Тест на удаление курса.
        """
        data = {"course": self.course.pk, "subscription": True, "user": self.user.pk}

        response = self.client.post('/subscription/create/', data=data)
        subscription_id = response.data['id']

        response = self.client.delete(f'/subscription/delete/{subscription_id}/', data=data)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(Subscription.objects.all().exists())
