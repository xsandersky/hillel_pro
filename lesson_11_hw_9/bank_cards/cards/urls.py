from django.urls import path, include
from rest_framework import routers

from .views.card_viewset import CardViewSet
from .views.card_view import activate_card, deactivate_card

router = routers.DefaultRouter()
router.register(r'', CardViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('activate/<str:pk>', activate_card),
    path('deactivate/<str:pk>', deactivate_card),
]