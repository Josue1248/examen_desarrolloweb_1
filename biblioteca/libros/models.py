from django.db import models
from django.conf import settings

# Create your models here.
class Libro(models.MOdel):
    Nombre= CharField(max_length=50,)
    Autor=CharField(max_length=50,)
    Editorial= CharField(max_length=50,)
    ISBN=CharField=(max_length=20,)
    Precio=DecimalField(max_length=10,)
    Creado=DataTimeField(auto_now_add=True)
        def __str__(self):
            return str(self.Nombre)
