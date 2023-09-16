import uuid

from django.db import models

from .user import User

class Meeting(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150)
    date = models.DateTimeField()
    create_date_meeting = models.DateTimeField(auto_now_add=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name='meeting_participants')

    def __str__(self):
        return self.title
