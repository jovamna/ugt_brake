from django.contrib import admin
from .models import Reunion, Calendario, Permiso, Seguridad, Convenio



# Register your models here.


class ReunionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description',  'download' )
    ordering = ('id', 'published')
    search_fields = ('title','description','download')
    date_hierarchy = 'published'
    list_filter = ('id','title')
    
class CalendarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description',  'download' )
    ordering = ('id', 'published')
    search_fields = ('title','description','download')
    date_hierarchy = 'published'
    list_filter = ('id','title')
 
class PermisoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description',  'download' )
    ordering = ('id', 'published')
    search_fields = ('title','description','download')
    date_hierarchy = 'published'
    list_filter = ('id','title')
    
class SeguridadAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description',  'download' )
    ordering = ('id', 'published')
    search_fields = ('title','description','download')
    date_hierarchy = 'published'
    list_filter = ('id','title')
    
class ConvenioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description',  'download' )
    ordering = ('id', 'published')
    search_fields = ('title','description','download')
    date_hierarchy = 'published'
    list_filter = ('id','title')
    

 
 
 
 
 
 
 
admin.site.register(Reunion, ReunionAdmin)
admin.site.register(Calendario, CalendarioAdmin)
admin.site.register(Permiso, PermisoAdmin)
admin.site.register(Seguridad, SeguridadAdmin)
admin.site.register(Convenio, ConvenioAdmin)
