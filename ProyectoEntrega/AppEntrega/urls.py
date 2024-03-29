from django.urls import path, include
from AppEntrega import views
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.static import serve
from django.urls import re_path

urlpatterns = [

    path('', views.inicio,name="inicio"),
    path ("estilo",views.estilo,name="estilo"),
    path("truco", views.truco,name="truco"),
    path("mago", views.mago,name="mago"),
    #path("estilo-formularios/", views.estilo_formularios,name="estilo-formularios"),
    path("mago-formularios/", views.mago_formularios,name="mago-formularios"),
    #path("truco-formularios/", views.truco_formularios,name="truco-formularios"),
    path ("listado-magos/",views.busqueda_magos, name="listado-magos"),
    #path ("buscar/", views.buscar, name="buscar"),
    path('leerMago', views.leerMago, name = "LeerMago"),
    path('eliminarMago/<mago_id>/',views.eliminarMago, name="eliminarMago"  ),
    path('editarMago/<mago_id>/',views.editarMago, name="editarMago"  ),
    path('login', views.login_request, name="login"),
    path('register', views.register, name='register'),
    #path('logout', LogoutView.as_view(template_name='AppEntrega/logout.html'), name='Logout'),
    path('agregar-avatar/', views.agregar_avatar, name='agregar_avatar'),
    path('sobre-mi/', views.sobre_mi, name='sobre-mi'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('comentarios/', views.comentarios, name='comentarios'),
    


] 
#urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]