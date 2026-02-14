from django.contrib import admin
from .models import Leccion, Ejercicio, ProgresoEstudiante

class EjercicioInline(admin.TabularInline):
    model = Ejercicio
    extra = 1
    fields = ['numero', 'enunciado', 'tipo', 'respuesta_correcta', 'puntos']

@admin.register(Leccion)
class LeccionAdmin(admin.ModelAdmin):
    list_display = ['numero', 'titulo', 'nivel', 'activa', 'fecha_creacion']
    list_filter = ['nivel', 'activa']
    search_fields = ['titulo', 'teoria']
    list_editable = ['activa']
    inlines = [EjercicioInline]
    
    fieldsets = (
        ('Información básica', {
            'fields': ('numero', 'titulo', 'descripcion', 'nivel')
        }),
        ('Contenido', {
            'fields': ('teoria', 'ejemplos'),
            'classes': ('wide',)
        }),
        ('Estado', {
            'fields': ('activa',)
        }),
    )

@admin.register(Ejercicio)
class EjercicioAdmin(admin.ModelAdmin):
    list_display = ['leccion', 'numero', 'tipo', 'puntos']
    list_filter = ['tipo', 'leccion']
    search_fields = ['enunciado']

@admin.register(ProgresoEstudiante)
class ProgresoEstudianteAdmin(admin.ModelAdmin):
    list_display = ['estudiante', 'leccion', 'completada', 'puntuacion', 'fecha_completada']
    list_filter = ['completada', 'leccion']
    search_fields = ['estudiante__username']
