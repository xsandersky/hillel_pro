import json
import uuid
from functools import reduce

from django.http import HttpRequest, HttpResponseRedirect, JsonResponse 
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from cards.models import Card

#from django.shortcuts import render


class CardView(View):
    def get(self, request:HttpRequest):
        cards = Card.objects.all()
        json_response = {"cards": [{"id": str(card.id),
                        "number": card.number,
                        "cvv": card.cvv,
                        "issue": card.issue,
                        "expiration": card.expiration,
                        "balance": card.balance,
                        "status": card.status} for card in cards]
                    }
        first = cards[1].expiration
        print(first, type(first))
        for card in cards:
            print(card.expiration)
        return JsonResponse(json_response)
