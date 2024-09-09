from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Registration
from .serializers import RegistrationSerializer
from events.models import Event
from django.core.mail import send_mail


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        event = Event.objects.get(id=self.request.data['event'])
        serializer.save(user=self.request.user, event=event)
        send_mail(
            'Registration Confirmation',
            f'You have registered for {event.title}',
            'from@example.com',
            [self.request.user.email]
        )
