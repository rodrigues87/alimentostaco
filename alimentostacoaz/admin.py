from django.contrib import admin

# Register your models here.
from alimentostacoaz.models import Alimento
from recomendado.models import Recomendado

admin.site.register(Alimento)
admin.site.register(Recomendado)