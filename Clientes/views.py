from django.shortcuts import render
from Clientes.models import Clientes
from Clientes import models
from django.http.response import HttpResponse
from .forms import ClientesForm

# Create your views here.

def index(request):


   obj=Clientes.objects.all()
   myForm=ClientesForm()
   if request.method=="POST":
      myForm=ClientesForm(request.POST)
      if myForm.is_valid():
         myForm.save()
      else:
         print("hubo un error en el registro")
   context={
         'form':myForm,
         'Clientes':obj,
         'ClientesForm' : ClientesForm
      }

   return render(request, 'Clientes.html', context)
   