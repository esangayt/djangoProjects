from django.urls import path, include

from packages.hospital.api.views import BusquedaView, BusquedaColeccionView

urlpatterns = [
    path('clinica/', include('packages.hospital.api.router')),
    path('api-auth/', include('rest_framework.urls')),
    path('busqueda/<str:busqueda>/', BusquedaView.as_view(), name='busqueda'),
    path('coleccion/<str:table>/<str:busqueda>/', BusquedaColeccionView.as_view(),
         name='busqueda-coleccion'),
]
