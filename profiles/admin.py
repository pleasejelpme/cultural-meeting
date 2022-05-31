from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Perfil

class PerfilAdmin(UserAdmin):
    list_display = (
        'email', 
        'username', 
        'fecha_creado',
        'is_admin',
        'is_staff'
        )
    
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'fecha_creado')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Perfil, PerfilAdmin)
     