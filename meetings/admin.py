from django.contrib import admin
from .models import Meeting, Ciudad, Comentario, Categoria

admin.site.register(Meeting)
admin.site.register(Comentario)
admin.site.register(Ciudad)
admin.site.register(Categoria)