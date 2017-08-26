from django.shortcuts import render

# Create your views here.
def listar_publicacion(request):
        return render (request, 'blog/listar_publicacion.html', {})
