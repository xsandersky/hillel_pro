from rest_framework import serializers
from .models import Meeting, Comment, Purchase




class MeetingSerializer(serializers.ModelSerializer):
    purchases = PurchaseSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Meeting
        fields = ['id', 'organizer', 'title', 'date', 'create_date_meeting', 'participants', 'purchases', 'comments']





