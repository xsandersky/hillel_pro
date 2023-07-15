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
        json_response = {
                "cards": [
                    {
                        "id": str(card.id),
                        "number": card.number,
                        "cvv": card.cvv,
                        "issue": card.issue,
                        "expiration": card.expiration,
                        "balance": card.balance,
                        "status": card.status
                        } 
                        for card in cards
                        ]
                    }
        if request.headers["accept"] == "application/json":
            return JsonResponse(json_response)
        else:
            context = {
                "cards": [
                    {
                        "number": card.number,
                        "cvv": card.cvv,
                        "issue": card.issue,
                        "expiration": card.expiration,
                        "balance": card.balance,
                        "status": card.status,
                        }
                        for card in cards
                ]
            }
            return render(request, "cards/cards_list.html", context, "text/html")


    def post(self, request: HttpRequest):
        body = json.loads(request.body)
        card = Card.objects.create(
            number=body["number"],
            cvv=body["cvv"],
            issue=body["issue"],
            expiration=body["expiration"],
            balance=body["balance"],
            status=body["status"] 
        )
        return JsonResponse({"id":str(card.id)})
    

def create_card_view(request):
    if request.method == "GET":
        cards = Card.objects.all()
        return render(request, "cards/create_card_form.html", {"cards": cards})
    elif request.method == "POST":
        Card.objects.create(
            number=request.POST["number"],
            cvv=request.POST["cvv"],
            issue=request.POST["issue"],
            expiration=request.POST["expiration"],
            balance=request.POST["balance"],
            status=request.POST["status"]
        )
        return HttpResponseRedirect(reverse("cards"))

    
def is_valid(self, number):
    LOOKUP = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)
    number = reduce(str.__add__, filter(str.isdigit, number))
    evens = sum(int(i) for i in number[-1::-2])
    odds = sum(LOOKUP[int(i)] for i in number[-2::-2])
    return ((evens + odds) % 10 == 0)
