from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from meeting.permissions import IsCommentAuthor
from meeting.models import Comment
from meeting.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsCommentAuthor, IsAuthenticated]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
