from django.db import models
from django.contrib.auth.models import User

class Leccion(models.Model):
    numero = models.IntegerField(unique=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    
    # Contenido de la lección
    teoria = models.TextField(help_text="Explicación teórica")
    ejemplos = models.TextField(help_text="Ejemplos prácticos")
    
    # Nivel
    NIVELES = [
        ('basico', 'Básico'),
        ('intermedio', 'Intermedio'),
        ('avanzado', 'Avanzado'),
    ]
    nivel = models.CharField(max_length=20, choices=NIVELES, default='basico')
    
    # Metadata
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['numero']
        verbose_name_plural = "Lecciones"
    
    def __str__(self):
        return f"Lección {self.numero}: {self.titulo}"


class Ejercicio(models.Model):
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE, related_name='ejercicios')
    numero = models.IntegerField()
    enunciado = models.TextField()
    
    TIPOS = [
        ('multiple_choice', 'Opción Múltiple'),
        ('completar', 'Completar'),
        ('verdadero_falso', 'Verdadero/Falso'),
    ]
    tipo = models.CharField(max_length=50, choices=TIPOS)
    opciones = models.JSONField(null=True, blank=True)
    respuesta_correcta = models.JSONField()
    explicacion = models.TextField()
    puntos = models.IntegerField(default=1)
    
    class Meta:
        ordering = ['numero']
    
    def __str__(self):
        return f"Ejercicio {self.numero} - Lección {self.leccion.numero}"


class ProgresoEstudiante(models.Model):
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE)
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE)
    completada = models.BooleanField(default=False)
    puntuacion = models.IntegerField(default=0)
    fecha_completada = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        unique_together = ['estudiante', 'leccion']
        verbose_name_plural = "Progresos de Estudiantes"
    
    def __str__(self):
        return f"{self.estudiante.username} - Lección {self.leccion.numero}"
