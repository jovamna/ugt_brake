from django.urls import path
#from .views import ReunionListView
from . import views




app_name = "comitiva"

urlpatterns=[
   #path('', ReunionListView.as_view(), name='home')
    #path('', HomeView.as_view(), name="home"),
    path('', views.manager, name='quienes-somos'),

]