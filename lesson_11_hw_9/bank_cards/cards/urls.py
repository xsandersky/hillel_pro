from django.urls import path

from .views.cards_views import CardView, create_card_view

urlpatterns = [
    path('', CardView.as_view(http_method_names=['get', 'post']), name='cards'),
    path('create', create_card_view, name='create_card_form'),
]
