from django.urls import path, include
from rest_framework import routers

from .views.card_viewset import CardViewSet
from .views.cards_views import CardView
from .views.card_view import activate_card, deactivate_card
from .views.task_view import TaskView

router = routers.DefaultRouter()
router.register(r'card', CardViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('card/<str:pk>/activate/', activate_card),
    path('card/<str:pk>/deactivate/', deactivate_card),
    path('task/', TaskView.as_view()),
    path('viewall/', CardView.as_view()),
]