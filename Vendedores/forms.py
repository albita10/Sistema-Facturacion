from django import forms
from django.forms import ModelForm
from Vendedores.models import Vendedores
#from .models import Post
#from django.forms import ArticuloForm


class VendedoresForm(ModelForm):
    nombre =forms.CharField()
    porciento_comision =forms.DecimalField(max_digits=10000)
    estado =forms.BooleanField()

    class Meta:
        model = Vendedores
        fields=[
            'nombre',
            'porciento_comision',
            'estado'
        ]

