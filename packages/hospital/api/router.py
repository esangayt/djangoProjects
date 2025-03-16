from rest_framework.routers import DefaultRouter

from packages.hospital.api.views import HospitalVS, UsuarioVS, DoctorVS

router = DefaultRouter()

router.register(r'hospital', HospitalVS, basename='hospital')
router.register(r'usuarios', UsuarioVS, basename='usuario')
router.register(r'medico', DoctorVS, basename='medico')

urlpatterns = router.urls
