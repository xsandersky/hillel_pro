from django.test import TestCase
from django.urls import reverse

from cards.models import Card
from cards.views.cards_views import CardView


# Create your tests here.
class CardsTest(TestCase):
    def test_get_cards(self):
        #given
        card = Card(number="1111-1111-1111-1111", cvv=123, issue="10/10",
                    expiration="10/20", balance=123, status="new")
        card.save()
        url = reverse("cards")

        #when
        responce = self.client.get(url).json()

        #then
        self.assertEquals(responce, {"cards": [{"id": str(card.id),
                                                "number": card.number,
                                                "cvv": card.cvv,
                                                "issue": card.issue,
                                                "expiration": card.expiration,
                                                "balance": card.balance,
                                                "status": card.status}]})


    def test_post_cards(self):
        #given
        url = reverse("cards")

        card = {"number": "2222-2222-2222-2222",
            "cvv": 456,
            "issue": "11/11",
            "expiration": "11/21",
            "balance": 456,
            "status": "new"}

        #when
        responce = self.client.post(url, card, content_type="application/json")

        #then
        self.assertEquals(responce.status_code, 200)
        new_card = Card.objects.get(number=card["number"])
        self.assertEqual(new_card.number, card["number"])
        self.assertEqual(new_card.cvv, card["cvv"])
        self.assertEqual(new_card.issue, card["issue"])
        self.assertEqual(new_card.expiration, card["expiration"])
        self.assertEqual(new_card.balance, card["balance"])
        self.assertEqual(new_card.status, card["status"])


class Is_Valid(TestCase):
    def test_is_valid(self):
        #given
        card = {"number": "4561-2612-1234-5467",
            "cvv": 456,
            "issue": "11/11",
            "expiration": "11/21",
            "balance": 456,
            "status": "new"}
        
        card_2 = {"number": "4561-2612-1234-5467",
            "cvv": 456,
            "issue": "11/11",
            "expiration": "11/21",
            "balance": 456,
            "status": "new"}
        
        #when
        answer = CardView.is_valid(card, '4561-2612-1234-5467')
        answer2 = CardView.is_valid(card_2, '4561-2612-1234-5464')

        #then
        assert answer == True
        assert answer2 == False

