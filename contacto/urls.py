from django.urls import path
from . import views

app_name = 'contacto'

urlpatterns = [
   path('', views.contact, name="contacto"),
    #path('newsletter/', views.suscribe, name='suscribirse'),
    #path('validate/', views.validate_email, name='validate_email'),
]