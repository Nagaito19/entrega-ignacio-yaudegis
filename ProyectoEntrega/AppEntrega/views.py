from django.shortcuts import render,redirect
from AppEntrega.models import *
from AppEntrega.forms import *
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Comentario 
from .forms import ComentarioForm 






def inicio(request):
    return render(request, "AppEntrega/inicio.html")
@login_required
def estilo(request):
    mi_estilo=Estilo.objects.all()

    if request.method =='POST':
        mi_formulario=EstiloFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion=mi_formulario.cleaned_data
            estilo=Estilo(nombre=informacion['estilo'])
            estilo.save()
            nuevo_estilo={'nombre':informacion['estilo']}
            return render(request,'AppEntrega\estilo.html', {'formulario_estilo':mi_estilo,
                                                            'nuevo_estilo':nuevo_estilo,
                                                            'mi_estilo':mi_estilo})
    else:
        mi_formulario=EstiloFormulario()

    return render(request, "AppEntrega\estilo.html", {'formulario_estilo':mi_formulario,'mi_estilo':mi_estilo})
@login_required
def truco (request):
    mi_truco=Truco.objects.all()

    if request.method =='POST':
        mi_formulario=TrucoFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion=mi_formulario.cleaned_data
            truco=Truco(nombre=informacion['truco'], clase=informacion['clase'])
            truco.save()
            nuevo_truco={'nombre':informacion['truco']}
            return render(request,'AppEntrega/truco.html', {'formulario_truco':mi_truco,
                                                            'nuevo_truco':nuevo_truco,
                                                            'mi_truco':mi_truco})
    else:
        mi_formulario=TrucoFormulario()

    return render(request, "AppEntrega/truco.html", {'formulario_truco':mi_formulario,'mi_truco':mi_truco})
@login_required
def mago (request):
    mi_mago=Mago.objects.all()

    if request.method =='POST':
        mi_formulario=MagoFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion=mi_formulario.cleaned_data
            mago=Mago(nombre=informacion['nombre'], apellido=informacion['apellido'])
            mago.save()
            nuevo_mago={'nombre':informacion['nombre']}
            return render(request,'AppEntrega/mago.html', {'formulario_mago':mi_mago,
                                                            'nuevo_mago':nuevo_mago,
                                                            'mi_mago':mi_mago})
    else:
        mi_formulario=MagoFormulario()

    return render(request, "AppEntrega/mago.html", {'formulario_mago':mi_formulario,'mi_mago':mi_mago})

def estilo_formularios(request):

    if request.method == 'POST':
        mi_formulario=EstiloFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion=mi_formulario.cleaned_data
            nuevo_estilo=Estilo(nombre=request.POST['estilo'])
            nuevo_estilo.save()
            return redirect('/AppEntrega/')
    mi_formulario= EstiloFormulario()
    return render(request,'AppEntrega/estilo-formularios.html', {"formulario_estilo":mi_formulario})

def mago_formularios(request):
    
    if request.method == 'POST':
        mi_formulario=MagoFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion=mi_formulario.cleaned_data
            nuevo_mago=Mago(nombre=informacion['nombre'],
                            apellido=informacion['apellido'])
            nuevo_mago.save()
            return redirect('/AppEntrega/')
    mi_formulario= MagoFormulario()
    return render(request,'AppEntrega/Mago-formularios.html', {"formulario_mago":mi_formulario})

def truco_formularios(request):
    
    if request.method == 'POST':
        mi_formulario=TrucoFormulario(request.POST)  

        if mi_formulario.is_valid():
            informacion=mi_formulario.cleaned_data
            nuevo_truco=Truco(nombre=informacion['nombre'],
                              clase=informacion['clase'])
            nuevo_truco.save()
            return redirect('/AppEntrega/')
    mi_formulario= TrucoFormulario()
    return render(request,'AppEntrega/truco-formularios.html', {"formulario_truco":mi_formulario})

def busqueda_magos(request):
    nombre_busqueda = request.GET.get('nombre')
    if nombre_busqueda:
         magos = Mago.objects.filter(nombre__icontains=nombre_busqueda)
    else:
        magos = Mago.objects.all()
    
    form = BusquedaMago()
    return render(request,'AppEntrega/listado-magos.html', {"listado_magos":magos, 'form': form})

def leerMago(request):
      mago = Mago.objects.all() #trae todos los mago

      contexto= {"mago":mago} 

      return render(request, "AppEntrega/leerMago.html",contexto)

def eliminarMago(request,mago_id):
    mago = Mago.objects.get(id=mago_id)
    mago.delete()

    mago=Mago.objects.all()
    contexto={"mago" : mago}
    return render(request, "AppEntrega/leerMago.html",contexto)

def editarMago(request,mago_id):
    mago=Mago.objects.get(id=mago_id)

    if request.method=='POST':
        mi_formulario = MagoFormulario(request.POST)

        print(mi_formulario)

        if mi_formulario.is_valid:
            informacion = mi_formulario.cleaned_data

            mago.nombre = informacion['nombre']
            mago.apellido = informacion['apellido']

            mago.save()

            return render(request,"AppEntrega/leerMago.html")
    else:
        mi_formulario=MagoFormulario(initial={'nombre':mago.nombre, 'apellido':mago.apellido})

    return render (request,"AppEntrega/editarMago.html", {"mi_formulario":mi_formulario,"mago_id":mago_id})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'AppEntrega/login.html', {'form': form})
        

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = UserCreationForm()
    return render(request, 'inicio/registro.html', {'form': form})
@login_required
def logout(request):
    logout(request)
    return render(request,"AppEntrega/logout.html", {"mensaje":"se ha salido con exito> "})


def agregar_avatar(request):
    if request.method == 'POST':
        mi_formulario = AvatarFormulario(data = request.POST,files = request.FILES)
        if mi_formulario.is_valid():
            u = User.objects.get(username=request.user)
            avatar= Avatar(user=u, imagen=mi_formulario.cleaned_data['imagen'])
            avatar.save()
            return render (request,'AppEntrega/inicio.html')
    
    else:

        mi_formulario= AvatarFormulario()
    return render(request,"AppEntrega/agregar-avatar.html", {"mi_formulario": mi_formulario})


def sobre_mi(request):
    return render(request, "AppEntrega/sobre-mi.html")

def comentarios(request):
    comentarios = Comentario.objects.order_by('-fecha') # obtiene los comentarios de la base de datos ordenados por fecha descendente
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save() # guarda el comentario en la base de datos
            return redirect('comentarios') # redirige al usuario a la página de comentarios
    else:
        form = ComentarioForm()
    return render(request, 'AppEntrega/comentarios.html', {'form': form, 'comentarios': comentarios})  