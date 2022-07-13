from django.contrib import admin
from django.urls import path, include
from .views import HomeView
from . import views
from django.conf import settings   #para descargar archivos
from django.conf.urls.static import static  #para descargar archivos
from django.views.static import serve
from django.conf.urls.i18n import i18n_patterns
import os  #para el secret admin
import environ  #para el secret admin



urlpatterns = [
    path('i18n/', include("django.conf.urls.i18n")),
    # Paths del admin
    #path(os.environ.get('SECRET_ADMIN_URL') + '/admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    path('politica-cookies', views.cookie, name="politica-cookies"),
    path('formacion', include('formacion.urls',  namespace="formacion")),
    path('descargas', include('descargas.urls',  namespace="descargas")),
    path('quienes-somos', include('comitiva.urls',  namespace="comitiva")),
    path('contacto', include('contacto.urls',  namespace="contacto")),
 
]

    
#produccion
if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns #(No sure)
    #urlpatterns += staticfiles_urlpatterns() #(no sure)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)    

                                                                                                                                                                      