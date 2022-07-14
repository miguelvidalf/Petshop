from django.contrib import admin
from .models import Categoria, Vehiculo, Producto , PerfilUsuario

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Vehiculo)
admin.site.register(Producto)
admin.site.register(PerfilUsuario)
