from django.db import transaction
from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from meeting.models import Purchase
from meeting.serializers import PurchaseSerializer

class PurchaseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    def perform_create(self, serializer):
        item = serializer.validated_data.get('item')
        price = serializer.validated_data.get('price')
        meeting = serializer.validated_data.get('meeting')
        users = serializer.validated_data.get('user')

        if not all(user in meeting.participants.all() for user in users):
            raise serializers.ValidationError("Не все пользователи из покупки участвуют во встрече")

        with transaction.atomic():
            purchase = Purchase.objects.create(item=item, price=price, meeting=meeting)
            purchase.user.set(users)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
