from customers.models import Client, Domain

# Crear el cliente
tenant = Client(
    schema_name='tenant1',
    name='Tenant 1',
    paid_until='2025-12-31',
    on_trial=True,
)
tenant.save()

# Asignar dominio
domain = Domain()
domain.domain = 'tenant1.localhost'  # ejemplo
domain.tenant = tenant
domain.is_primary = True
domain.save()

from django_tenants.utils import schema_context
from customers.models import Client

tenant = Client.objects.get(schema_name='tenant1')

with schema_context(tenant.schema_name):
    from django.contrib.auth.models import User

    User.objects.create_superuser(username='admin', email='admin@tenant1.com',
                                  password='123456')

# py manage.py create_tenant  --schema_name=tenant2  --name="Cliente Uno S.A."
# --paid_until=2025-12-31 --on_trial="True"  --domain-domain=tenant2.localhost  --domain-is_primary="True"
