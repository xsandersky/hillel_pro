from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APIClient
from rest_framework import status
from .models import Meeting, Comment, Purchase


class MeetingTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.meeting = Meeting.objects.create(
            title='Test Meeting',
            date=timezone.now(),  # Указываем значение для поля date
            organizer=self.user
        )
        self.url = reverse('add_user_to_meeting', kwargs={'pk': self.meeting.pk})

    def test_add_user_to_meeting(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.user in self.meeting.participants.all())

    def test_add_user_to_meeting_already_participant(self):
        self.client.force_login(self.user)
        self.meeting.participants.add(self.user)  # Add user as a participant
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class CommentTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.meeting = Meeting.objects.create(
            title='Test Meeting',
            date='2023-09-16 18:00:00',
            organizer=self.user,
        )
        self.client = APIClient()
        self.client.login(username='testuser', password='testpassword')

    def test_create_comment(self):
        data = {
            'comment': 'Test Comment',
            'user': self.user.id,
            'meeting': self.meeting.id,
        }
        url = reverse('comment-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.get().comment, 'Test Comment')

    def test_update_comment(self):
        comment = Comment.objects.create(
            comment='Initial Comment',
            user=self.user,
            meeting=self.meeting,
        )
        data = {'comment': 'Updated Comment'}
        url = reverse('comment-detail', args=[comment.id])
        response = self.client.patch(url, data, format='json')  # Заменить .put на .patch
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        comment.refresh_from_db()  # Обновляем объект из базы данных
        self.assertEqual(comment.comment, 'Updated Comment')

    def test_list_comments(self):
        Comment.objects.create(
            comment='Comment 1',
            user=self.user,
            meeting=self.meeting,
        )
        Comment.objects.create(
            comment='Comment 2',
            user=self.user,
            meeting=self.meeting,
        )
        url = reverse('comment-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_delete_comment(self):
        comment = Comment.objects.create(
            comment='To be deleted',
            user=self.user,
            meeting=self.meeting,
        )
        url = reverse('comment-detail', args=[comment.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.count(), 0)

class PurchaseViewSetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpassword')

        # Создаем встречу и добавляем пользователя
        self.meeting = Meeting.objects.create(
            title='Test Meeting',
            date='2023-09-16 18:00:00',
            organizer=self.user,
        )
        self.meeting.participants.add(self.user)  # Добавляем пользователя к встрече

    def test_create_purchase(self):
        data = {
            'item': 'Test Item',
            'price': 100,
            'meeting': self.meeting.id,
            'user': [self.user.id],
        }
        url = reverse('purchase-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Purchase.objects.count(), 1)
        self.assertEqual(Purchase.objects.get().item, 'Test Item')
        self.assertEqual(Purchase.objects.get().price, 100)

    def test_create_purchase_not_participants(self):
        another_user = User.objects.create_user(username='anotheruser', password='anotherpassword')
        data = {
            'item': 'Test Item',
            'price': 100,
            'meeting': self.meeting.id,
            'user': [another_user.id],
        }
        url = reverse('purchase-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_purchase(self):
        purchase = Purchase.objects.create(
            item='Initial Item',
            price=50,
            meeting=self.meeting,
        )
        data = {
            'item': 'Updated Item',
            'price': 75,
            'meeting': self.meeting.id,
            'user': [self.user.id],
        }
        url = reverse('purchase-detail', args=[purchase.id])
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Purchase.objects.get().item, 'Updated Item')
        self.assertEqual(Purchase.objects.get().price, 75)

class MeetingChecksViewTestCase(TestCase):
    def setUp(self):
        # Создаем двух пользователей
        self.user1 = User.objects.create_user(username='user1', password='password1')
        self.user2 = User.objects.create_user(username='user2', password='password2')

        # Создаем встречу и добавляем пользователей в участники
        self.meeting = Meeting.objects.create(
            title='Test Meeting',
            date='2023-09-16 18:00:00',
            organizer=self.user1,
        )
        self.meeting.participants.add(self.user1, self.user2)

        # Создаем покупку, разделяемую между пользователями
        self.purchase = Purchase.objects.create(
            item='Test Item',
            price=100,
            meeting=self.meeting,
        )
        self.purchase.user.add(self.user1, self.user2)

        # Создаем клиент API
        self.client = APIClient()
        self.client.login(username='user1', password='password1')

    def test_meeting_checks_view(self):
        url = reverse('meeting-check', args=[self.meeting.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверяем, что полученный чек верно распределен
        check_data = response.data['check']
        self.assertEqual(check_data['user1'], 50)  # user1 получает 50% от 100
        self.assertEqual(check_data['user2'], 50)  # user2 получает 50% от 100
