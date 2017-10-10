from django.shortcuts import render
from .models import libros

# Create your views here.
def Home(request):
    print request
    wb="Bienvenido"
    wb2={"Usuario":"Miguel"}
    return render(request,"home.html",{'wb':wb, 'wb2',wb2})
