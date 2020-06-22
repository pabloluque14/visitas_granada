from django.contrib import admin

# Register your models here.

from .models import Visita
from .models import Comentario

admin.site.register(Visita)
admin.site.register(Comentario)