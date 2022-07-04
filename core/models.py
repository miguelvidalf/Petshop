from distutils.command.upload import upload
import email
from unittest.util import _MAX_LENGTH
from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
=======
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
>>>>>>> 8dae587b0230a27859873833e9c6b54382accbb3

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
<<<<<<< HEAD
    
# Crear perfil usuario

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=80, blank=True, null=True, verbose_name="Rut")
    direccion = models.CharField(max_length=80, blank=True, null=True, verbose_name="Dirección")

    def __str__(self):
        return f"{self.user.username} - {self.user.first_name} {self.user.last_name} ({self.user.email})"
=======




class Usuario(abstractBaseUser):
    username = models.CharField('Nombre de usuario',unique = True, max_length=100)
    email = models.EmailField('Correo electronico', max_length=300, unique = True)
    nombre = models.CharField('Nombre', max_length=300, blank= True, null = True)
    apellidos = models.CharField('Apellidos', max_length=300, blank=True, null= True)
    imagen = models.ImageField('Imagen de perfil', upload_to='perfil/', height_field=None, width_field=None, max_lenght=300)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador =models.BooleanField(default=False)
    objects = usuario_administrador 
    USERNAME_FIELD ="username"
    REQUIRED_FIELDS =['email','nombre','apellido',]
    def __str__(self):
        return f'{self.nombre},{self.apellido}'
    def has_perm(self,perm,obj = None):
        return True 
    def has_module_perms(self,app_label):
        return True
    @property
    def is_staff(self):
        return self.usuario_administrador


class UsuarioAdministrador(BaseUserManager):
    def create_user(self,email,username,nombre,apellidos,password = None):
        if not email:
            raise ValueError('El usuario debe tener un correo electronico!')

        usuario = self.model(
        username = username,
        email = self.normalize_email(email),
        nombre = nombre,
        apellidos = apellidos
    
        )
        usuario.set_password(password)
        usuario.save()
        return usuario
    def create_superuser(self,username,email,nombre,apellidos,password):
        usuario = self.create_user(
            email,
            username = username,
            nombre = nombre,
            apellidos = apellidos
        )

        usuario.usuario_administrador = True
        usuario.save()
        return usuario


    
>>>>>>> 8dae587b0230a27859873833e9c6b54382accbb3

