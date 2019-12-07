from django.db import models
from multiselectfield import MultiSelectField
import datetime
from Clientes.models import Clientes

tipo_movimiento=(
    ('DB','Transacción Débito'),
    ('CR','Saldo a Favor del Contribuyente')
)
# Create your models here.
class Asientos(models.Model):
    descripcion = models.CharField(max_length=200,default="")
    Clientes = models.ForeignKey(Clientes,on_delete=models.CASCADE)
    cuenta = models.CharField(max_length=11)
    tipo_movimiento = MultiSelectField(max_length=200,choices=tipo_movimiento)
    fecha_asiento = models.DateField(null=True)
    monto = models.DecimalField(decimal_places=3,max_digits=10000,default=0)
    estado = models.BooleanField(default=True)

    def __str__(selt):
        return "{}".format(self.descricpcion)


