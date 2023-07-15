from django.test import TestCase
from django.urls import reverse
from django.shortcuts import render

class TestCreateCardFormTemplate(TestCase):
    def test_create_card_form_template(self):
        response = self.client.get(reverse('create_card_form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cards/create_card_form.html')
        self.assertContains(response, '<form')  # Проверяем наличие формы
        self.assertContains(response, '<input type="text" name="number"')  # Проверяем наличие полей ввода
        self.assertContains(response, '<input type="text" name="cvv"')  # Проверяем наличие полей ввода
        self.assertContains(response, '<input type="text" name="issue"')  # Проверяем наличие полей ввода
        self.assertContains(response, '<input type="text" name="expiration"')  # Проверяем наличие полей ввода
        self.assertContains(response, '<input type="text" name="balance"')  # Проверяем наличие полей ввода
        self.assertContains(response, '<input type="text" name="status"')  # Проверяем наличие полей ввода
        self.assertContains(response, '<input type="submit" value="Create"')  # Проверяем наличие кнопки отправки формы
