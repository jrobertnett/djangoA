from django.conf.urls import include, url
from . import views

urlpatterns = [

    url(r'^$', views.listar_publicacion ),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detalle_pub, name = 'postear'),
    url(r'^postear/nuevo/$', views.nueva_publicacion, name='nueva_publicacion'),
    url(r'^postear/(?P<pk>[0-9]+)/editar/$', views.editar_publicacion, name='editar_publicacion'),
]
