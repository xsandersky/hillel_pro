import uuid

from django.db import models

from .user import User
from .meeting import Meeting


class Purchase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.CharField(max_length=250, blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    user = models.ManyToManyField(User)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name='purchases')
