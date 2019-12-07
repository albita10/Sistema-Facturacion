from django import forms
from Clientes.models import Clientes
#from django.forms import ArticuloForm


class ClientesForm(forms.ModelForm):
    nombre_comercial = forms.CharField(max_length=40)
    cedula = forms.CharField(max_length=40)
    cuenta = forms.CharField(max_length=40)
    estado = forms.BooleanField()

    class Meta:
        model=Clientes
        fields=[
            'nombre_comercial',
            'cedula',
            'cuenta',
            'estado'
        ]

