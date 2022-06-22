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
