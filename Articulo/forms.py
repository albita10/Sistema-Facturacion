from django import forms
from django.forms import ModelForm
from Articulo.models import Articulo
#from .models import Post
#from django.forms import ArticuloForm


class ArticuloForm(ModelForm):
    descripcion =forms.CharField()
    precio =forms.DecimalField(max_digits=10000)
    estado =forms.BooleanField()

    class Meta:
        model = Articulo
        fields=[
            'descripcion',
            'precio',
            'estado'
        ]

