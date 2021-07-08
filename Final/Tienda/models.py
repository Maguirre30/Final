from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Seccion(models.Model):
    nomCateg = models.CharField(max_length=64, null=False)

    def __str__(self):
        return f"{self.nomCateg}"

class Producto(models.Model):

    def __str__(self):
        return self.nombre
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, related_name="clasificacion_seccion")
    nombre = models.CharField(max_length=250, null=False)
    precio = models.CharField(max_length=2000, null=False)
    detalles = models.TextField()
    imagen = models.CharField(max_length=300)

class Cart(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario")
    carrito = models.ManyToManyField(Producto)

    def __str__(self):
        return f"{self.usuario} - {self.carrito}"

class Order(models.Model):
    items = models.CharField(max_length=1000)
    nombre = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    cpostal = models.CharField(max_length=100)
    total = models.CharField(max_length=200)