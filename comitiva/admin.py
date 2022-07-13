from django.contrib import admin
from .models import Manager, Group


# Register your models here.
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'cargo', 'area',  'turno', 'admin_image') #
    ordering = ( 'name', 'cargo', 'area', 'turno')
    search_fields = ('name','cargo','area', 'turno')
    list_filter = ('name','cargo')


  
 
      
    
    
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'cargo', 'area',  'turno', 'foto_group' )#
    ordering = ( 'name', 'cargo', 'area',)
    search_fields = ('name','cargo','area', 'turno')
    list_filter = ('name','cargo', 'area', 'turno')
    

    
    
 
admin.site.register(Manager, ManagerAdmin)
admin.site.register(Group, GroupAdmin)