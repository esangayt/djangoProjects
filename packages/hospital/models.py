from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    img = models.URLField(blank=True, null=True)
    role = models.CharField(max_length=50, default='USER_ROLE')
    google = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.username


class Hospital(models.Model):
    nombre = models.CharField(max_length=255)
    img = models.URLField(blank=True, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Medico(models.Model):
    nombre = models.CharField(max_length=255)
    img = models.URLField(blank=True, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre