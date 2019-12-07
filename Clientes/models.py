from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre_comercial = models.TextField(blank=True,null=True)
    cedula = models.CharField(max_length=40,null=False,unique=True,)
    cuenta = models.CharField(max_length=40)
    estado = models.BooleanField(default=True)

    def __str__(selt):
        return selt.nombre_comercial


