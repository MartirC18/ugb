from django.contrib import admin

# Register your models here.
from .models import VEHICULOS,CLIENTES,EMPLEADOS,Registro

admin.site.register(VEHICULOS)
admin.site.register(CLIENTES)
admin.site.register(EMPLEADOS)
admin.site.register(Registro)

