from django.db import models

# Create your models here.
class Vendedores(models.Model):
    nombre = models.TextField(blank=True,null=True)
    porciento_comision = models.DecimalField(decimal_places=3,max_digits=10000,default=0)
    estado = models.BooleanField(default=True)

    def __str__(selt):
        return selt.nombre


