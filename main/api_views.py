from rest_framework import viewsets, status
from .models import Appointment
from .serializers import AppointmentSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        start = serializer.validated_data['start']
        end = serializer.validated_data['end']
        # overlap check
        if Appointment.objects.filter(start__lt=end, end__gt=start).exists():
            raise ValidationError({"detail": "Time slot already taken."})
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
