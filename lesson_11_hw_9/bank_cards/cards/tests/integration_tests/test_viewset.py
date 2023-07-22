from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from cards.models import Card

class CardViewSetTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
    def test_create_card(self):
        data = data = {
            'number': '1',
            'cvv': '1',
            'issue': '1/1',
            'expiration': '1/10',
            'balance': 1,
            'status': 'new',
            'title': 'Test Card',
            'owner': 1,
        }
        response = self.client.post('/api/cards/', data)
        self.assertEqual(Card.objects.count(), 1)
        self.assertEqual(Card.objects.get().title, 'Test Card')
        self.assertEqual(Card.objects.get().owner, self.user)
        
    def test_update_card(self):
        card = Card.objects.create(number='2', cvv=2, issue='2/2', expiration='2/22', balance=2, \
                                   status='new', title='Old Title', owner=self.user)
        data = {
            'title': 'New Title',
        }

        response = self.client.patch(f'/api/cards/{card.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        card.refresh_from_db()
        self.assertEqual(card.title, 'New Title')

    def test_update_card_other_user(self):
        other_user = User.objects.create_user(username='other_user', password='other_password')
        card = Card.objects.create(number='2', cvv=2, issue='2/2', expiration='2/22', balance=2, \
                                   status='new', title='Other User Card', owner=self.user)

        data = {
            'title': 'Updated Title',
        }

        response = self.client.patch(f'/api/cards/{card.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        card.refresh_from_db()
        self.assertEqual(card.title, 'Other User Card')

    def test_activate_card(self):
        response = self.client.post(f'/activate/{self.card.id}/')
        self.card.refresh_from_db()
        self.assertEqual(self.card.status, 'active')

    def test_deactivate_card(self):
        response = self.client.post(f'/deactivate/{self.card.id}/')
        self.card.refresh_from_db()
        self.assertEqual(self.card.status, 'block')
