from django.test import TestCase
from django.urls import reverse
from django.shortcuts import render
from cards.models import Card

class CardsListTemplateTest(TestCase):
    def test_cards_list_template(self):
        # Создаем несколько карточек для проверки
        card1 = Card.objects.create(number="1111-5555-4444-9999", cvv=123, issue="01/22", expiration="01/25", balance=10450, status="active")
        card2 = Card.objects.create(number="1111-5555-1111-4444", cvv=456, issue="02/23", expiration="02/26", balance=20000, status="new")

        # Проверяем отображение шаблона cards_list.html при другом значении заголовка 'Accept'
        response = self.client.get(reverse('cards'), **{'HTTP_ACCEPT': 'text/html'})  # Установка заголовка 'Accept'
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cards/cards_list.html')
        self.assertContains(response, '<table>')
        self.assertContains(response, '<th>Number</th>')
        self.assertContains(response, f'<td>{card1.number}</td>')
        self.assertContains(response, f'<td>{card2.number}</td>')
        self.assertContains(response, 'Add new card')
