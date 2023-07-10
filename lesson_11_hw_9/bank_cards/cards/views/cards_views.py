import json
import uuid
from functools import reduce

from django.http import HttpRequest, JsonResponse
from django.views import View

from cards.models import Card

#from django.shortcuts import render


class CardView(View):

    def get(self, request:HttpRequest):
        cards = Card.objects.all()
        return JsonResponse(
            {
                'cards': [{'id': str(card.id),
                        'number': card.number,
                        'cvv': card.cvv,
                        'issue': card.issue,
                        'expiration': card.expiration,
                        'balance': card.balance,
                        'status': card.status} for card in cards]})


    def post(self, request: HttpRequest):
        body = json.loads(request.body)
        card = Card(number=body["number"],
                     cvv=body["cvv"],
                     issue=body["issue"],
                     expiration=body["expiration"],
                     balance=body["balance"],
                     status=body["status"])
        card.save()
        return JsonResponse({'id':str(card.id)})
    
    
    def is_valid(self, number):
        LOOKUP = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)
        number = reduce(str.__add__, filter(str.isdigit, number))
        evens = sum(int(i) for i in number[-1::-2])
        odds = sum(LOOKUP[int(i)] for i in number[-2::-2])
        return ((evens + odds) % 10 == 0)
