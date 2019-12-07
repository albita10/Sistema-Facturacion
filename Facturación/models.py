from django.db import models
import datetime
from Clientes.models import Clientes
from Vendedores.models import Vendedores
from Articulo.models import Articulo

# Create your models here.
class Facturación(models.Model):
    Vendedores = models.ForeignKey(Vendedores,on_delete=models.CASCADE)
    Clientes = models.ForeignKey(Clientes,on_delete=models.CASCADE)
    fecha = models.DateField(null=True)
    comentario = models.CharField(max_length=200)
    Articulo = models.ForeignKey(Articulo,on_delete=models.CASCADE)
    cantidad =models.FloatField(default=0)
    precio_unitario = models.DecimalField(decimal_places=3,max_digits=100,default=0)

    def __str__(selt):
        return "{}".format(self.Vendedores)


