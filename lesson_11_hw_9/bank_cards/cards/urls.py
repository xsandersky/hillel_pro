from django.urls import path

from .views.cards_views import CardView

urlpatterns = [
    path('', CardView.as_view(http_method_names=['get', 'post']), name='cards'),
]
