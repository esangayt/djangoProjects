from django.contrib import admin
from packages.hospital.models import Usuario, Hospital, Medico


# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    pass


admin.site.register(Hospital)
admin.site.register(Medico)
