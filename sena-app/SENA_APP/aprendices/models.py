from django.db import models

# Create your models here.

class Aprendiz(models.Model):
    documento_identidad = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    fecha_nacimiento = models.DateField()
    correo_electronico = models.EmailField(unique=True, null=True, blank=True)
    ciudad = models.CharField(max_length=100, null=True, blank=True)
    programa = models.CharField(max_length=100, null=True, blank=True, verbose_name="Programa de Formación")

    class Meta:
        verbose_name = "Aprendiz"
        verbose_name_plural = "Aprendices"
        ordering = ['nombre', 'apellido']

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"