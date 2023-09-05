import uuid
from django.db import models


class Meeting(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    place_of_meeting = models.CharField(max_length=75)
    date_of_meeting = models.DateField()
    create_meeting = models.DateTimeField(auto_now_add=True)
    update_meeting = models.DateTimeField(auto_now=True)

