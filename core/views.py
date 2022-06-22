
from django.shortcuts import redirect, render
from .models import Producto, Vehiculo, Categoria
from .forms import VehiculoForm, ProductoForm

# Create your views here.

def home(request):
    return render(request, "core/home.html")

def nosotros(request):
    return render(request, "core/nosotros.html")

def ingreso(request):
    return render(request, "core/ingreso.html")

def misDatos(request):
    return render(request, "core/misDatos.html")
def misCompras(request):
    return render(request, "core/misCompras.html")

def indexPetshop(request):
    data = {"list": Producto.objects.all().order_by('idProducto')}
    return render(request, "core/indexPetshop.html", data)

def registro(request):
    return render(request, "core/registro.html")

def vehiculo_tienda(request):
    data = {"list": Vehiculo.objects.all().order_by('patente')}
    return render(request, "core/vehiculo_tienda.html", data)

def vehiculo_ficha(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)
    data = {"vehiculo":  vehiculo}
    return render(request, "core/vehiculo_ficha.html", data)

def producto_ficha(request, id):
    producto = Producto.objects.get(idProducto=id)
    data = {"producto":  producto}
    return render(request, "core/producto_ficha.html", data)

def vehiculo(request, action, id):
    data = {"mesg": "", "form": VehiculoForm, "action": action, "id": id}

    if action == 'ins':
        if request.method == "POST":
            form = VehiculoForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡El vehículo fue creado correctamente!"
                except:
                    data["mesg"] = "¡No se puede crear dos vehículos con la misma patente!"

    elif action == 'upd':
        objeto = Vehiculo.objects.get(patente=id)
        if request.method == "POST":
            form = VehiculoForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡El vehículo fue actualizado correctamente!"
        data["form"] = VehiculoForm(instance=objeto)

    elif action == 'del':
        try:
            Vehiculo.objects.get(patente=id).delete()
            data["mesg"] = "¡El vehículo fue eliminado correctamente!"
            return redirect(vehiculo, action='ins', id = '-1')
        except:
            data["mesg"] = "¡El producto ya estaba eliminado!"

    data["list"] = Vehiculo.objects.all().order_by('patente')
    return render(request, "core/vehiculo.html", data)

def producto(request, action, id):
    data = {"mesg": "", "form": ProductoForm, "action": action, "id": id}

    if action == 'ins':
        if request.method == "POST":
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡El producto fue creado correctamente!"
                except:
                    data["mesg"] = "¡No se pueden crear dos productos con el mismo id."

    elif action == 'upd':
        objeto = Producto.objects.get(idProducto=id)
        if request.method == "POST":
            form = ProductoForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡El Producto fue actualizado correctamente!"
        data["form"] = ProductoForm(instance=objeto)

    elif action == 'del':
        try:
            Producto.objects.get(idProducto=id).delete()
            data["mesg"] = "¡El producto fue eliminado correctamente!"
            return redirect(producto, action='ins', id = '-1')
        except:
            data["mesg"] = "¡El producto ya estaba eliminado!"

    data["list"] = Producto.objects.all().order_by('idProducto')
    return render(request, "core/producto.html", data)

def poblar_bd(request):
    Vehiculo.objects.all().delete()
    Vehiculo.objects.create(patente="ALAN67", marca='Volvo', modelo="Volvo Station Wagon", imagen="images/volvosw.jpg", categoria=Categoria.objects.get(idCategoria=2))
    Vehiculo.objects.create(patente="BILL88", marca='Saleen', modelo="S7", imagen="images/saleen.jpg", categoria=Categoria.objects.get(idCategoria=2))
    Vehiculo.objects.create(patente="ELVI54", marca='Shelby', modelo="Cobra de 1967", imagen="images/cobra.jpg", categoria=Categoria.objects.get(idCategoria=2))
    Vehiculo.objects.create(patente="FEDE84", marca='Mercedes-Benz', modelo="Pagoda de 1972", imagen="images/pagoda.jpg", categoria=Categoria.objects.get(idCategoria=2))
    Vehiculo.objects.create(patente="JEFF46", marca='Ford', modelo="Wolf WR1 Ford Race Car", imagen="images/wolf.jpg", categoria=Categoria.objects.get(idCategoria=2))
    Vehiculo.objects.create(patente="JOHN80", marca='Ford', modelo="Flathead Roadster de 1932", imagen="images/flathead.jpg", categoria=Categoria.objects.get(idCategoria=2))
    Vehiculo.objects.create(patente="PAUL62", marca='Rolls-Royce', modelo="Phantom", imagen="images/phantom.jpg", categoria=Categoria.objects.get(idCategoria=2))
    Vehiculo.objects.create(patente="SCAR47", marca='Mustang', modelo="Mustang de 1970", imagen="images/mustang.jpg", categoria=Categoria.objects.get(idCategoria=2))
    Vehiculo.objects.create(patente="TIRO98", marca='Mercedes-Benz', modelo="Iron Bike de 1998", imagen="images/motoiron.jpg", categoria=Categoria.objects.get(idCategoria=3))
    Vehiculo.objects.create(patente="UVAM20", marca='Silver Plus', modelo="Silver de 2000", imagen="images/silver.jpg", categoria=Categoria.objects.get(idCategoria=3))
    return redirect(vehiculo, action='ins', id = '-1')

def poblar_bd_producto(request):
    Producto.objects.all().delete()
    Producto.objects.create(idProducto="0001",nombre='Bandanas Azul-Negro-Rojo', precio='$7.990', descripcion='Bandanas con diseño exclusivo en distintos colores' , imagen="images/bandana-1.jpg", categoria=Categoria.objects.get(idCategoria=4))
    Producto.objects.create(idProducto="0002",nombre='Cama azul', precio='$7.990', descripcion='Cama azul felpuda' , imagen="images/cama-2.jpg", categoria=Categoria.objects.get(idCategoria=4))
    return redirect(producto,action='ins',id = '-1')
