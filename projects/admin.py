from django.contrib import admin

from .models import Destinatarios, Proyecto, Usuario_registrado
admin.site.register (Proyecto)
admin.site.register(Usuario_registrado)
admin.site.register(Destinatarios)
