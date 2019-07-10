from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(ComunidadEnergetica)
admin.site.register(Gestor)
admin.site.register(InscritoComunidad)
