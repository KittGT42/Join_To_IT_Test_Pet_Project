from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer
from rest_framework import viewsets


@permission_classes([IsAuthenticated])
class EventCreateView(APIView):
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(organizer=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()  # Укажите queryset
    serializer_class = EventSerializer
