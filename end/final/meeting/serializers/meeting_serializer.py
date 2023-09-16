from rest_framework import serializers

from meeting.models import Meeting
from .comment_serializer import CommentSerializer
from .purchase_serializer import PurchaseSerializer


class MeetingSerializer(serializers.ModelSerializer):
    purchases = PurchaseSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Meeting
        fields = ['id', 'organizer', 'title', 'date', 'create_date_meeting', 'participants', 'purchases', 'comments']
