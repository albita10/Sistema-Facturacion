from django.shortcuts import render
from Facturación.models import Facturación
from Asientos import models
from django.http.response import HttpResponse
from .forms import FacturaciónForm
# Create your views here.

def index(request):


    obj=Facturación.objects.all()
    myForm=FacturaciónForm()
    if request.method=="POST":
      myForm=FacturaciónForm(request.POST)
    if myForm.is_valid():
        myForm.save()
    else:
        print("hubo un error en el registro")
    context={
        'form':myForm,
        'Facturación':obj,
        'FacturaciónForm' : FacturaciónForm()
    }
    return render(request, 'Facturación.html', context)
   