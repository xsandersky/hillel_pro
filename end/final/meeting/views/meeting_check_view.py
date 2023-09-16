from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from meeting.models import Meeting
from meeting.serializers import MeetingSerializer


class MeetingChecksView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        participants = instance.participants.all()
        purchases = instance.purchases.all()

        check_dict = {}

        for purchase in purchases:
            purchase_users = purchase.user.all()
            share = purchase.price / len(purchase_users)

            for user in purchase_users:
                if user in participants:
                    check_dict[user.username] = check_dict.get(user.username, 0) + share

        return Response({'meeting': MeetingSerializer(instance).data, 'check': check_dict})