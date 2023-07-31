from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from cards.tasks import activate_card

class TaskView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        result = activate_card.apply_async(args=[request.data['id']])
        return Response(data=str(result), status=204)
