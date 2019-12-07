from django import forms
from Facturación.models import Facturación
from django.forms import Select
import datetime
#from .models import Post
#from django.forms import ArticuloForm


class FacturaciónForm(forms.ModelForm):
    class Meta:
        model=Facturación
        fields=[
            'Vendedores',
            'Clientes',
            'fecha',
            'comentario',
            'Articulo',
            'cantidad',
            'precio_unitario'
        ]

        widgets={
            "Vendedores": Select(),
            "Clientes" : Select(),
            "Articulo" : Select(),
        }
        

