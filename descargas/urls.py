from django.urls import path
#from .views import ReunionListView
from . import views
#from .views import HomeView



app_name = "descargas"

urlpatterns=[
   #path('', ReunionListView.as_view(), name='home')
    #path('', HomeView.as_view(), name="home"),
    path('reuniones', views.reunion, name='reuniones'),
    path('calendario', views.calendario, name='calendario'),
    path('permisos', views.permisos, name='permisos'),
    path('prevencion', views.prevencion, name='prevencion'),
    path('convenio', views.convenio, name='convenio'),
]