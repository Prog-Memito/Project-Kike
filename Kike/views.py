from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from os import remove, path
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request, 'Kike/home.html')

def man(request):
    return render(request, 'Kike/catalogo.html')

def woman(request):
    return render(request, 'Kike/catalogo.html')

def kids(request):
    return render(request, 'Kike/catalogo.html')

def login(request):
    return render(request, 'registration/login.html')

def register(request):

    data={
        'form':UserForm()
    }

    if request.method=='POST':
        formulario=UserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Logeo exitoso")
            #redirige al index
            return redirect(to='home')
        data["form"]=formulario

    return render(request, 'registration/register.html', data)

def profile(request):
    return render(request, 'Kike/profile.html')

def exit(request):  
    logout(request)
    
    return redirect('home')

def admin(request):
    return render(request, 'Kike/admin.html')

def tilla(request):

    tillas=Tilla.objects.all()
    page=request.GET.get('page', 1)

    try:
        paginator=Paginator(tillas, 5)
        tillas=paginator.page(page)
    except:
        raise Http404
    
    datos={
        'entity':tillas,
        'paginator':paginator
    }

    return render(request, 'Kike/tilla.html', datos)

def add_tilla(request):

    datos={
        'form':TillaForm()
    }

    if request.method == "POST":
        formulario = TillaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Zapatilla agregada")
            return redirect(to="tilla")
        else:
            datos["form"] = formulario
    
    return render(request, 'Kike/add-tilla.html', datos)

def view_tilla(request, id):

    tilla=get_object_or_404(Tilla, id=id)

    datos={
        'tilla':tilla
    }

    return render(request, 'Kike/ver-tilla.html', datos)

def mod_tilla(request, id):

    tilla=get_object_or_404(Tilla, id=id)
    
    data={
        'form':UpdateTillaForm(instance=tilla)
    }

    if request.method == "POST":
        formulario=UpdateTillaForm(data=request.POST, instance=tilla, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Zapatilla modificada")
            return redirect(to="tilla")
        data["form"]=formulario

    return render(request, 'Kike/mod-tilla.html', data)

def del_tilla(request, id):

    tilla=get_object_or_404(Tilla, id=id)
    
    if request.method=="POST":
        
        #from os import remove, path
        #from django.conf import settings
        remove(path.join(str(settings.MEDIA_ROOT).replace('/media',''))+tilla.foto.url)
        tilla.delete()
        return redirect(to="tilla")
        
    datos={
        "tilla":tilla
    }

    return render(request, 'Kike/del-tilla.html', datos)

def serie(request):

    serie=Serie.objects.all()
    page=request.GET.get('page',1)

    try:
        paginator=Paginator(serie, 5)
        serie=paginator.page(page)
    except:
        raise Http404
    
    datos={
        'entity':serie,
        'paginator':paginator
    }

    return render(request, 'Kike/serie.html', datos)

def add_serie(request):

    datos={
        'form':SerieForm()
    }

    if request.method=="POST":
        formulario=SerieForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Serie agregado")
            return redirect(to="serie")
        else:
            datos["form"]=formulario

    return render(request, 'Kike/add-serie.html', datos)

def del_serie(request, id=id):

    serie = get_object_or_404(Serie, id=id)
    serie.delete()
    messages.warning(request, "Serie eliminada")
    
    return redirect(to=serie)