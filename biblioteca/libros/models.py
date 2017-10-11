from django.db import models
from django.conf import settings

# Create your models here.
class  Libro (models.Model):
    Nombre= models.CharField(max_length =200)
    Autor= models.CharField(max_length =200)
    Editorial= models.CharField(max_length =200)
    ISBN= models.CharField(max_length =200)
    Precio= models.FloatField()
    Creado= models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.Nombre+': '+self.Autor)
