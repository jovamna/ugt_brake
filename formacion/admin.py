from django.contrib import admin
from .models import Formacion


# Register your models here.
class FormacionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',  'image_formacion')
    ordering = ( 'title', 'description')
    search_fields = ('title','description')
    list_filter = ('title','description')


  
 

    

    
    
 
admin.site.register(Formacion, FormacionAdmin)