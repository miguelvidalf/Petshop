from distutils.command.upload import upload
import email
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models here.

# Create Modelo para Categoria

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de categoría")
    nombreCategoria = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre de la categoría")

    def __str__(self):
        return self.nombreCategoria

# Create Modelo para vehículo

class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True, verbose_name="Patente")
    marca = models.CharField(max_length=80, blank=False, null=False, verbose_name="Marca vehículo")
    modelo = models.CharField(max_length=80, null=True, blank=True, verbose_name="Modelo")
    imagen = models.ImageField(upload_to="images/", default="sinfoto.jpg", null=False, blank=False, verbose_name="Imagen")
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.patente
    
# Create modelo para producto

class Producto(models.Model):
    idProducto = models.CharField(max_length=6, primary_key=True, verbose_name="idProducto")
    nombre = models.CharField(max_length=80, blank=False, null=False, verbose_name="NombreProducto")
    precio = models.CharField(max_length=80, blank=False, null=False, verbose_name="Precio")
    descripcion = models.CharField(max_length=80, blank=False, null=False, verbose_name="Descripcion")
    disponibilidad = models.CharField(max_length=80, blank=False, null=False, verbose_name="disponibilidad")
    imagen = models.ImageField(upload_to="images/", default="sinfoto.jpg", null=False, blank=False, verbose_name="Imagen")
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.idProducto
    
# Crear perfil usuario

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=80, blank=True, null=True, verbose_name="Rut")
    direccion = models.CharField(max_length=80, blank=True, null=True, verbose_name="Dirección")
    es_suscriptor = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.user.username} - {self.user.first_name} {self.user.last_name} ({self.user.email})"

