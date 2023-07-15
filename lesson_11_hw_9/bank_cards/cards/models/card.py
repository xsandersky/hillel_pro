import uuid
from django.db import models


class Card(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.CharField(max_length=20)
    cvv = models.PositiveSmallIntegerField()
    issue = models.CharField(max_length=10)
    expiration = models.CharField(max_length=10)
    balance = models.IntegerField()
    status = models.CharField(max_length=20)
