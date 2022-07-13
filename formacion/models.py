from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.safestring import mark_safe



class Formacion(models.Model):
    
    
    def image_formacion(self):
        return mark_safe('<a href="/media/%s"><img src="/media/%s" width=50px height=50px /></a>'%(self.image,self.image))
    
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    image = models.ImageField(upload_to='formacion/', blank=True, null=True,verbose_name="Imagen") # allow none`
    link = models.URLField(max_length=500, null=True, blank=True, verbose_name="Dirección Web")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    
    
    class Meta:
        verbose_name = "formacion"
        verbose_name_plural = "formaciones"
        ordering = ["-created"]

    def __str__(self):
        return self.title