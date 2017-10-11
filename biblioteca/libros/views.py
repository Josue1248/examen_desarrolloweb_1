from django.shortcuts import render
from .models import Libro

# Create your views here.
def home(request):
    print request
    return render(request, 'home.html')

def lista_libros(request):
    result_set = Libro.objects.all()
    context = {"result": result_set}
    return render(request, "lista_libros.html", context)


def detalle_libros(request, id=10):
    result_set = Libro.objects.get(id=id)
    context = {"result": result_set}
    return render(request, "detalle_libro.html", context)
