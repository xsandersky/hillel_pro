import uuid
from django.db import models


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment = models.TextField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()


