from django.shortcuts import render
from .models import libros

# Create your views here.
def Home(request):
    print request
    wb="Bienvenido"
    wb2={"Usuario":"Miguel"}
    return render(request,"home.html",{'wb':wb, 'wb2',wb2})

def lista_libros(request):
    result_set = Libros.objects.all()
    context = {"result": result_set}
    return render(request, "lista_libros.html", context)


def detalle_libros(request, id=10):
    result_set = Libros.objects.get(id=id)
    context = {"result": result_set}
    return render(request, "detalle_libro.html", context)
