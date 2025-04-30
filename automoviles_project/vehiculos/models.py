from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class Automovil(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField(
        validators=[
            MinValueValidator(1990),
            MaxValueValidator(datetime.datetime.now().year)
        ]
    )
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"

