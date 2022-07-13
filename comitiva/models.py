from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.safestring import mark_safe




class Manager(models.Model):
    def admin_image(self):
        return mark_safe('<a href="/media/%s"><img src="/media/%s" width=50px height=50px /></a>'%(self.photo,self.photo))
     
    #admin_image.allow_tags = True
    #admin_image.short_description = 'Image'
    
    name = models.CharField(max_length=150)
    cargo = models.CharField(max_length=150)
    area = models.CharField(max_length=150)
    turno = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='gallery/', blank=True, null=True,) # allow none`

    def __str__(self):
        return self.name
    

        


class Group(models.Model):
    
    def foto_group(self):
        return mark_safe('<a href="/media/%s"><img src="/media/%s" width=50px height=50px /></a>'%(self.photo,self.photo))
    
    name = models.CharField(max_length=150)
    cargo = models.CharField(max_length=150)
    area = models.CharField(max_length=150)
    turno = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='gallery/', blank=True, null=True,) # allow none`

    def __str__(self):
        return self.name
    
    
    

# Create your models here.
