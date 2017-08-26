from django.shortcuts import render

# Create your views here.
def listar_publicacion(request):
    publi = Publicar.objects.filter(fecha_publica_lte=timezone.now()).order_by ('fecha_publica')
    return render (request, 'blog/listar_publicacion.html', {'publi':publi})
