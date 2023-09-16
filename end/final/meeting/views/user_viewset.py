from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from meeting.serializers import UserSerializer
from meeting.models import User


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
