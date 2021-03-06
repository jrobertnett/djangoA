from django.conf.urls import include, url
from . import views

urlpatterns = [

    url(r'^$', views.listar_publicacion, name='listar_publicacion' ),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detalle_pub, name = 'postear'),
    url(r'^postear/nuevo/$', views.nueva_publicacion, name='nueva_publicacion'),
    url(r'^postear/(?P<pk>[0-9]+)/editar/$', views.editar_publicacion, name='editar_publicacion'),
    url(r'^borrador/$', views.borradores_publicacion, name= 'borradores_publicacion'),
    url(r'^postear/(?P<pk>\d+)/Publicar/$',views.postear_publicacion, name= 'postear_publicacion'),
    url(r'^postear/(?P<pk>\d+)/remover/$',views.remover_publicacion, name= 'remover_publicacion' ),
]
