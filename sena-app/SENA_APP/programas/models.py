from django.db import models

class Programa(models.Model):
    # --- CHOICES ---
    NIVEL_FORMACION_CHOICES = [
        ('AUX', 'Auxiliar'),
        ('OPE', 'Operario'),
        ('TEC', 'Técnico'),
        ('TGL', 'Tecnólogo'),
        ('ESP', 'Especialización Tecnológica'),
        ('COM', 'Complementario'),
    ]

    MODALIDAD_CHOICES = [
        ('PRE', 'Presencial'),
        ('VIR', 'Virtual'),
        ('MIX', 'Mixta'),
    ]

    ESTADO_CHOICES = [
        ('ACT', 'Activo'),
        ('INA', 'Inactivo'),
        ('SUS', 'Suspendido'),
        ('CAN', 'Cancelado'),
    ]

    # --- CAMPOS (FIELDS) ---
    codigo = models.CharField(max_length=20, unique=True, verbose_name="Código del Programa")
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Programa")
    nivel_formacion = models.CharField(max_length=3, choices=NIVEL_FORMACION_CHOICES, verbose_name="Nivel de Formación")
    modalidad = models.CharField(max_length=3, choices=MODALIDAD_CHOICES, default='PRE', verbose_name="Modalidad")
    duracion_meses = models.PositiveIntegerField(verbose_name="Duración en Meses")
    duracion_horas = models.PositiveIntegerField(verbose_name="Duración en Horas") # Nuevo campo
    descripcion = models.TextField(verbose_name="Descripción del Programa")
    competencias = models.TextField(verbose_name="Competencias a Desarrollar") # Nuevo campo
    perfil_egreso = models.TextField(verbose_name="Perfil de Egreso") # Nuevo campo
    requisitos_ingreso = models.TextField(verbose_name="Requisitos de Ingreso") # Nuevo campo
    centro_formacion = models.CharField(max_length=200, verbose_name="Centro de Formación") # Nuevo campo
    regional = models.CharField(max_length=100, verbose_name="Regional") # Nuevo campo
    estado = models.CharField(max_length=3, choices=ESTADO_CHOICES, default='ACT', verbose_name="Estado")
    fecha_creacion = models.DateField(verbose_name="Fecha de Creación del Programa")
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")

    class Meta:
        verbose_name = "Programa de Formación"
        verbose_name_plural = "Programas de Formación"
        ordering = ['nombre']

    # **CORRECCIÓN CLAVE:** El método debe ser __str__ (doble guión bajo) y devolver una cadena.
    def __str__(self):
        return f"{self.nombre} ({self.codigo})"