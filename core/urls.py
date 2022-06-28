from django.urls import path
from .views import home, poblar_bd, poblar_bd_producto, vehiculo, vehiculo_tienda, vehiculo_ficha, producto, producto_ficha, carritoCompra
from .views import nosotros,indexPetshop, registro, ingreso, misDatos, misCompras

urlpatterns = [
    path('', home, name="home"),
    path('poblar_bd', poblar_bd, name="poblar_bd"),
    path('indexPetshop/', indexPetshop, name="indexPetshop"),
    path('vehiculo/<action>/<id>', vehiculo, name="vehiculo"),
    path('producto/<action>/<id>', producto, name="producto"),
    path('vehiculo_tienda', vehiculo_tienda, name="vehiculo_tienda"),
    path('vehiculo_ficha/<id>', vehiculo_ficha, name="vehiculo_ficha"),
    path('producto_ficha/<id>', producto_ficha, name="producto_ficha"),
    path('poblar_bd_producto', poblar_bd_producto, name="poblar_bd_producto"),
    path('nosotros',nosotros, name="nosotros"),
    path('registro', registro, name="registro"),
    path('ingreso/', ingreso, name="ingreso"),
    path('misDatos/', misDatos, name="misDatos"),
    path('misCompras/', misCompras, name="misCompras"),
    path('carritoCompra/', carritoCompra, name="carritoCompra"),
]
