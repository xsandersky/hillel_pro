from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cards.models import Card
from cards.card_serializer import CardSerializer, PatchSerializer
from cards.permissions import IsOwner


class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]
    queryset = Card.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = Card.objects.filter(owner_id=user)
            return queryset
        else:
            return Card.objects.none()
    

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)
    

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PatchSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
