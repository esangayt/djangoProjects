from rest_framework import viewsets, status
from rest_framework import permissions

from packages.hospital.api.serializers import UsuarioSerializer
from packages.hospital.models import Hospital, Usuario, Medico


class HospitalVS(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = UsuarioSerializer

    # permission_classes = [permissions.IsAuthenticated]


class UsuarioVS(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    # permission_classes = [permissions.IsAuthenticated]


class DoctorVS(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = UsuarioSerializer

    # permission_classes = [permissions.IsAuthenticated]
# python manage.py migrate hospital zero
# python manage.py migrate admin zero
# python manage.py migrate
