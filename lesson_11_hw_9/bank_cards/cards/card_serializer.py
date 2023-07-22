from rest_framework import serializers

from cards.models import Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class PatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'title']
