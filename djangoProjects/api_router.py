from django.urls import path, include

urlpatterns = [
    path('clinica/', include('packages.hospital.api.router'))
]
