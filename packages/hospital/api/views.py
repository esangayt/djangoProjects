from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView

from packages.hospital.api.serializers import UsuarioSerializer, HospitalSerializer, \
    MedicoSerializer
from packages.hospital.models import Hospital, Usuario, Medico


class HospitalVS(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

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


class BusquedaView(APIView):
    def get(self, request, busqueda):
        search_field = busqueda or ""

        usuarios = Usuario.objects.filter(nombre__icontains=search_field)
        medicos = Medico.objects.filter(nombre__icontains=search_field)
        hospitales = Hospital.objects.filter(nombre__icontains=search_field)

        usuarios_serializados = UsuarioSerializer(usuarios, many=True)
        medicos_serializados = MedicoSerializer(medicos, many=True)
        hospitales_serializados = HospitalSerializer(hospitales, many=True)

        return Response({
            "ok": True,
            "usuarios": usuarios_serializados.data,
            "medicos": medicos_serializados.data,
            "hospitales": hospitales_serializados.data,
        })
