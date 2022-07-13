from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Reunion(models.Model):
    id = models.BigAutoField(
        primary_key=True,
    )

    title = models.CharField(
        max_length=150,
        verbose_name='Title'
    )


    description = models.TextField(
        max_length=500,
        verbose_name='Description',
         null=True,
        blank=True
    )
    
    published = models.DateTimeField(default=timezone.now)

    download = models.FileField(
        upload_to='reunion/'
    )





class Calendario(models.Model):
    id = models.BigAutoField(
        primary_key=True,
    )

    title = models.CharField(
        max_length=150,
        verbose_name='Title'
    )


    description = models.TextField(
        max_length=500,
        verbose_name='Description',
         null=True,
        blank=True
    )
    
    published = models.DateTimeField(default=timezone.now)

    download = models.FileField(
        upload_to='calendario/'
    )
    
    
    
    
    

class Permiso(models.Model):
    id = models.BigAutoField(
        primary_key=True,
    )

    title = models.CharField(
        max_length=150,
        verbose_name='Title'
    )


    description = models.TextField(
        max_length=500,
        verbose_name='Description',
         null=True,
        blank=True
    )
    
    published = models.DateTimeField(default=timezone.now)

    download = models.FileField(
        upload_to='permiso/'
    )
    
    
    
    
    

# Create your models here.

class Seguridad(models.Model):
    id = models.BigAutoField(
        primary_key=True,
    )

    title = models.CharField(
        max_length=150,
        verbose_name='Title'
    )


    description = models.TextField(
        max_length=500,
        verbose_name='Description',
         null=True,
        blank=True
    )
    
    published = models.DateTimeField(default=timezone.now)

    download = models.FileField(
        upload_to='seguridad/'
    )



# Create your models here.

class Convenio(models.Model):
    id = models.BigAutoField(
        primary_key=True,
    )

    title = models.CharField(
        max_length=150,
        verbose_name='Title'
    )


    description = models.TextField(
        max_length=500,
        verbose_name='Description',
         null=True,
        blank=True
    )
    
    published = models.DateTimeField(default=timezone.now)

    download = models.FileField(
        upload_to='convenio/', blank=True, null=True
    )

# Create your models here.
