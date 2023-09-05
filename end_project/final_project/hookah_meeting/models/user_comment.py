import uuid
from django.db import models

from .comment import Comment
from .user_meeting import UserMeeting


class UserComment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user_meeting = models.ForeignKey(UserMeeting, on_delete=models.CASCADE)
