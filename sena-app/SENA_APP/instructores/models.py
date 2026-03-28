from django.db import models

# Create your models here.

class Instructor(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjería'),
        ('TI', 'Tarjeta de Identidad'),
        ('PAS', 'Pasaporte'),
    ]
    
    NIVEL_EDUCATIVO_CHOICES = [
        ("TEC", "Técnico"),
        ("TGL", "Tecnólogo"),
        ("PRE", "pregrado"),
        ("ESP", "Especialización"),
        ("MAE", "Maestría"),
        ("DOC", "Doctorado"),
        
    ]
    
    tipo_documento = models.CharField(max_length=3, choices=TIPO_DOCUMENTO_CHOICES)
    numero_documento = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)
    ciudad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    nivel_educativo = models.CharField(max_length=3, choices=NIVEL_EDUCATIVO_CHOICES)
    especialidad = models.CharField(max_length=100)
    anos_experiencia = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)
    fecha_vinculacion = models.DateField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"
    
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
    