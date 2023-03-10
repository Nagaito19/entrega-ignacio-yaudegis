from django.urls import path, include
from AppEntrega import views
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings


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
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppEntrega/logout.html'), name='Logout'),



] 
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)