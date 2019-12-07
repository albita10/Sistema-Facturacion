from django.shortcuts import render
from Articulo.models import Articulo
from Articulo import models
from django.http.response import HttpResponse
from .forms import ArticuloForm
# Create your views here.

def index(request):


    obj=Articulo.objects.all()
    myForm=ArticuloForm()
    if request.method=="POST":
      myForm=ArticuloForm(request.POST)
    if myForm.is_valid():
        myForm.save()
    else:
        print("hubo un error en el registro")
    context={
        'form':myForm,
        'Articulo':obj,
        'ArticuloForm' : ArticuloForm()
    }
    return render(request, 'Articulo.html', context)
   