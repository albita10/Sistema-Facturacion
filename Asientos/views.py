from django.shortcuts import render
from Asientos.models import Asientos
from Asientos import models
from django.http.response import HttpResponse
from .forms import AsientosForm
# Create your views here.

def index(request):


    obj=Asientos.objects.all()
    myForm=AsientosForm()
    if request.method=="POST":
      myForm=AsientosForm(request.POST)
    if myForm.is_valid():
        myForm.save()
    else:
        print("hubo un error en el registro")
    context={
        'form':myForm,
        'Asientos':obj,
        'AsientosForm' : AsientosForm()
    }
    return render(request, 'Asientos.html', context)
   