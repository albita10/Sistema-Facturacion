from django import forms
from Asientos.models import Asientos
from django.forms import Select
import datetime
#from .models import Post
#from django.forms import ArticuloForm


class AsientosForm(forms.ModelForm):
    class Meta:
        model=Asientos
        fields=[
            'descripcion',
            'Clientes',
            'cuenta',
            'tipo_movimiento',
            'fecha_asiento',
            'monto',
            'estado'
        ]

        widgets={
            "Clientes" : Select(),
        }
        

