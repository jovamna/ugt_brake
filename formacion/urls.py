from django.urls import path
#from .views import ReunionListView
from . import views
#from .views import HomeView



app_name = "formacion"

urlpatterns=[
   #path('', ReunionListView.as_view(), name='home')
    #path('', HomeView.as_view(), name="home"),
    path('', views.formacion, name='formacion'),
    
]