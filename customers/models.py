from django_tenants.models import TenantMixin, DomainMixin
from django.db import models


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)

    # Campo obligatorio: si se debe crear el esquema automáticamente
    auto_create_schema = True


class Domain(DomainMixin):
    pass
