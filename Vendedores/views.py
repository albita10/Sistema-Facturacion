from django.shortcuts import render
from Vendedores.models import Vendedores
from Vendedores import models
from django.http.response import HttpResponse
from .forms import VendedoresForm

# Create your views here.

def index(request):


   obj=Vendedores.objects.all()
   myForm=VendedoresForm()
   if request.method=="POST":
      myForm=VendedoresForm(request.POST)
      if myForm.is_valid():
         myForm.save()
      else:
         print("hubo un error en el registro")
   context={
         'form':myForm,
         'Vendedores':obj,
         'VendedoresForm' : VendedoresForm
      }

   return render(request, 'Vendedores.html', context)
   