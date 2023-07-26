from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from cards.tasks import long_calculate

class TaskView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        long_calculate.apply_async(args=[request.data['x'], request.data['y']])
        return Response(status=204)