import uuid
from django.db import models

from .user_meeting import UserMeeting


class Purchase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_description = models.TextField()
    total_check = models.IntegerField()
    check_1_person = models.IntegerField()
    user = models.ForeignKey(UserMeeting, on_delete=models.CASCADE, related_name='purchase_for_user')
    meeting = models.ForeignKey(UserMeeting, on_delete=models.CASCADE, related_name='purchase_for_meeting')

    def count_participant_person(self):
        list_users_count = UserMeeting.objects.filter(meeting=self.meeting)
        users_count = list_users_count.count()
        if users_count > 0 and self.total_check is not None:
            self.check_1_person = int(self.total_check) / users_count
        else:
            self.check_1_person = int('0')
        self.save()




