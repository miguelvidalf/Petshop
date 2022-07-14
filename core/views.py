
from django.shortcuts import redirect, render
from .models import Producto, Vehiculo, Categoria,PerfilUsuario, PrBodega
from .forms import VehiculoForm, ProductoForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import RegistrarUsuarioForm, PerfilUsuarioForm, IniciarSesionForm, PrBodegaForm

# Create your views here.

def home(request):
    data = {"list": Producto.objects.all().order_by('idProducto')}
    return render(request, "core/home.html", data)

def nosotros(request):
    return render(request, "core/nosotros.html")

def carritoCompra(request):
    return render(request, "core/carritoCompra.html")

def api_ropa(request):
    return render(request, "core/api_ropa.html")

def misCompras(request):
    return render(request, "core/misCompras.html")

def indexPetshop(request):
    data = {"list": Producto.objects.all().order_by('idProducto')}
    return render(request, "core/indexPetshop.html", data)

def registro(request):
    return render(request, "core/registro.html")

def menuAdministrador(request):
    return render(request, "core/menuAdministrador.html")

def historialDeVentas(request):
    return render(request, "core/historialDeVentas.html")

def detalleDeFacturas(request):
    return render(request, "core/detalleDeFacturas.html")

def mantenedorUsuario(request):
    return render(request, "core/mantenedorUsuario.html")

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

#VIEW POBLAR BASE DE DATOS
def poblar_bd_producto(request):
    Producto.objects.all().delete()
    Producto.objects.create(idProducto="0001",nombre='Bandanas Azul-Negro-Rojo', precio='$7.990', descripcion='Bandanas con diseño exclusivo en distintos colores' , imagen="images/bandana-1.jpg", categoria=Categoria.objects.get(idCategoria=4))
    Producto.objects.create(idProducto="0002",nombre='Cama azul', precio='$7.990', descripcion='Cama azul felpuda' , imagen="images/cama-2.jpg", categoria=Categoria.objects.get(idCategoria=4))
    return redirect(producto,action='ins',id = '-1')

def ingreso(request):
    data = {"mesg": "", "form": IniciarSesionForm()}

    if request.method == "POST":
        form = IniciarSesionForm(request.POST)
        if form.is_valid:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(home)
                else:
                    data["mesg"] = "¡La cuenta o la password no son correctos!"
            else:
                data["mesg"] = "¡La cuenta o la password no son correctos!"
    return render(request, "core/ingreso.html", data)

def cerrar_sesion(request):
    logout(request)
    return redirect(home)

def registro(request):
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            rut = request.POST.get("rut")
            direccion = request.POST.get("direccion")
            PerfilUsuario.objects.update_or_create(user=user, rut=rut, direccion=direccion)
            return redirect(ingreso)
    form = RegistrarUsuarioForm()
    return render(request, "core/registro.html", context={'form': form})

def misDatos(request):
    data = {"mesg": "", "form": PerfilUsuarioForm}

    if request.method == 'POST':
        form = PerfilUsuarioForm(request.POST)
        if form.is_valid():
            user = request.user
            user.first_name = request.POST.get("first_name")
            user.last_name = request.POST.get("last_name")
            user.email = request.POST.get("email")
            user.save()
            perfil = PerfilUsuario.objects.get(user=user)
            perfil.rut = request.POST.get("rut")
            perfil.direccion = request.POST.get("direccion")
            perfil.save()
            data["mesg"] = "¡Sus datos fueron actualizados correctamente!"

    perfil = PerfilUsuario.objects.get(user=request.user)
    form = PerfilUsuarioForm()
    form.fields['first_name'].initial = request.user.first_name
    form.fields['last_name'].initial = request.user.last_name
    form.fields['email'].initial = request.user.email
    form.fields['rut'].initial = perfil.rut
    form.fields['direccion'].initial = perfil.direccion
    data["form"] = form
    return render(request, "core/misDatos.html", data)

def mantenedorDeBodega(request,action,id):
    if not (request.user.is_authenticated and request.user.is_staff):
        return redirect(home)

    data = {"mesg": "", "form": PrBodegaForm, "action": action, "id": id, "formsesion": IniciarSesionForm}

    if action == 'ins':
        if request.method == "POST":
            form = PrBodegaForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡El producto se  agregó correctamente!"
                except:
                    data["mesg"] = "¡No se pueden generar dos productos con el mismo codigo!"

    elif action == 'upd':
        objeto = PrBodega.objects.get(idbodega=id)
        if request.method == "POST":
            form = PrBodegaForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡el producto fue actualiado correctamente!"
        data["form"] = PrBodegaForm(instance=objeto)

    elif action == 'del':
        try:
            PrBodega.objects.get(idbodega=id).delete()
            data["mesg"] = "¡el producto fue eliminado correctamente!"
            return redirect(mantenedorDeBodega, action='ins', id = '-1')
        except:
            data["mesg"] = "¡eL PRODUCTO ya estaba eliminado!"

    data["list"] = PrBodega.objects.all().order_by('idbodega')
    return render(request, "core/mantenedorDeBodega.html", data)