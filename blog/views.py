from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Publicar
from.forms import PostearForm

def listar_publicacion(request):
    publi = Publicar.objects.filter(fecha_publica__lte=timezone.now()).order_by ('fecha_publica')
    return render (request, 'blog/listar_publicacion.html', {'publi':publi})

def detalle_pub(request, pk):
        p = get_object_or_404(Publicar, pk=pk)
        return render(request, 'blog/detalle_publicacion.html', {'p': p})

def nueva_publicacion(request):
        if request.method == "POST":
            f = PostearForm(request.POST)
            if f.is_valid():
                p = f.save(commit=False)
                p.autor = request.user
                p.fecha_publica = timezone.now()
                p.save()
                return redirect('postear', pk=p.pk)
        else:
            f = PostearForm()
        return render(request, 'blog/nueva_publicacion.html', {'f': f})

def editar_publicacion(request, pk):
        p = get_object_or_404(Publicar, pk=pk)
        if request.method == "POST":
            f = PostearForm(request.POST, instance=p)
            if f.is_valid():
                p = f.save(commit=False)
                p.autor = request.user
                p.save()
                return redirect('postear', pk=p.pk)
        else:
            f = PostearForm(instance=p)
        return render(request, 'blog/editar_publicacion.html', {'f': f})
