from django.contrib import admin
from .models import *

class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "comision")

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "mail")
    
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "mail", "profesion")

class EntregasAdmin(admin.ModelAdmin):
    list_display = ("nombre", "fecha", "entrega")

# Register your models here.
admin.site.register(Curso, CursoAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Entregable, EntregasAdmin)

