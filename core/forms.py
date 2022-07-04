from django import forms
from django.forms import ModelForm, fields
from .models import Vehiculo, Producto

class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['patente', 'marca', 'modelo', 'imagen', 'categoria']

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['idProducto', 'nombre', 'precio', 'descripcion','disponibilidad', 'imagen','categoria']


class myUser(AbstractUser):
    
    rut = models.CharField("Rut",max_length=10)
    dirusu = models.CharField("Direccion",max_length=300)
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
    def __str__(self):
        full_name = '%s %s' %(self.first_name, self.last_name)
        return full_name.strip()
