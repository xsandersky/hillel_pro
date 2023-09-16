from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required


from meeting.models import Meeting
from meeting.serializers import MeetingSerializer


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

    permission_classes = [IsAuthenticated]

@login_required
def add_user_to_meeting(request, pk):
    meeting = get_object_or_404(Meeting, pk=pk)
    user = request.user

    if user not in meeting.participants.all():
        meeting.participants.add(user)
        return JsonResponse({"message": f"Вы успешно добавлены во встречу {meeting.title}"}, status=status.HTTP_200_OK)
    else:
        return JsonResponse({"message": f"Вы уже участвуете во встрече {meeting.title}"},
                            status=status.HTTP_400_BAD_REQUEST)
