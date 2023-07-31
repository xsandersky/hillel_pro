import time
from datetime import datetime

from celery import shared_task
from cards.models import Card


@shared_task
def activate_card(pk:str):
    time.sleep(1)
    Card.objects.filter(pk=pk).update(status='active')
    return 'Success'


@shared_task
def deactivate_card():
    today_not_formated = datetime.today().strftime('%m/%Y')         #12/2023
    current_date = today_not_formated[:3] + today_not_formated[5:]  #12/23
    current_year = int(current_date[3:])
    current_month = int(current_date[:2])

    cards = Card.objects.all()
    for card in cards:
        card_month = int(card.expiration[:2])
        card_year = int(card.expiration[3:])
        if current_year > card_year or current_year == card_year and current_month > card_month:
            card.deactivate_card(card.id)

    return "Success"
