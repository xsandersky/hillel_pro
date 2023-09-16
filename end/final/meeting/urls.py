from django.urls import path, include
from rest_framework import routers

from meeting import views
from meeting.views import (MeetingChecksView, MeetingViewSet, CommentViewSet, PurchaseViewSet, UserViewSet,
                           add_user_to_meeting)

router = routers.DefaultRouter()
router.register(r"meeting", MeetingViewSet)
router.register(r"purchase", PurchaseViewSet)
router.register(r"comments", CommentViewSet)
router.register(r'login', UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('meeting/<uuid:pk>/check/', MeetingChecksView.as_view(), name='meeting-check'),
    path('meeting/add_user/<uuid:pk>/', views.add_user_to_meeting, name='add_user_to_meeting'),
]
