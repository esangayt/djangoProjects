from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


def validate_image_size(image):
    max_file_size = 5 * 1024 * 1024  # 5 MB
    if image.size > max_file_size:
        raise ValidationError("El tamaño del archivo debe ser menor a 5MB.")


class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    img = models.ImageField(upload_to='usuarios',
                            validators=[
                                validate_image_size,
                                FileExtensionValidator(
                                    allowed_extensions=['jpg', 'jpeg', 'png']),
                            ])
    role = models.CharField(max_length=50, default='USER_ROLE')
    google = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.username

    def clean(self):
        super().clean()


class Hospital(models.Model):
    nombre = models.CharField(max_length=255)
    img = models.ImageField(upload_to='hospitales',
                            validators=[
                                validate_image_size,
                                FileExtensionValidator(
                                    allowed_extensions=['jpg', 'jpeg', 'png']),
                            ])
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Medico(models.Model):
    nombre = models.CharField(max_length=255)
    img = models.ImageField(upload_to='medicos',
                            validators=[
                                validate_image_size,
                                FileExtensionValidator(
                                    allowed_extensions=['jpg', 'jpeg', 'png']),
                            ])
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
