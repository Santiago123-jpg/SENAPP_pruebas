import os
import django
from datetime import datetime, timedelta
from random import randint, choice

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SENA_APP.settings')
django.setup()

from programas.models import Programa
from instructores.models import Instructor
from cursos.models import Curso, InstructorCurso, AprendizCurso
from aprendices.models import Aprendiz

# Limpiar datos existentes
print("Limpiando datos existentes...")
Aprendiz.objects.all().delete()
Curso.objects.all().delete()
Instructor.objects.all().delete()
Programa.objects.all().delete()

# ========== CREAR PROGRAMAS ==========
print("Creando Programas...")
programas_data = [
    {
        'codigo': 'ADSO',
        'nombre': 'Desarrollo de Software Empresarial',
        'nivel_formacion': 'TEC',
        'modalidad': 'MIX',
        'duracion_meses': 24,
        'duracion_horas': 1920,
        'descripcion': 'Programa de formación en desarrollo de software',
        'competencias': 'Programación, Bases de datos, Desarrollo web',
        'perfil_egreso': 'Analista y desarrollador de software',
        'requisitos_ingreso': 'Bachiller completo',
        'centro_formacion': 'Centro de Servicios Financieros',
        'regional': 'Distrito Capital',
        'fecha_creacion': '2023-01-15',
    },
    {
        'codigo': 'SIGA',
        'nombre': 'Seguridad Informatica Aplicada',
        'nivel_formacion': 'TEC',
        'modalidad': 'PRE',
        'duracion_meses': 18,
        'duracion_horas': 1440,
        'descripcion': 'Programa en seguridad informática',
        'competencias': 'Seguridad, Redes, Administración',
        'perfil_egreso': 'Especialista en seguridad informática',
        'requisitos_ingreso': 'Bachiller completo',
        'centro_formacion': 'Centro de Electricidad y Electronica',
        'regional': 'Distrito Capital',
        'fecha_creacion': '2023-02-20',
    },
    {
        'codigo': 'ADTI',
        'nombre': 'Administracion Integral de Sistemas',
        'nivel_formacion': 'TGL',
        'modalidad': 'VIR',
        'duracion_meses': 24,
        'duracion_horas': 1920,
        'descripcion': 'Tecnólogo en administración de sistemas',
        'competencias': 'Linux, Windows Server, Redes',
        'perfil_egreso': 'Administrador de sistemas informáticos',
        'requisitos_ingreso': 'Bachiller completo',
        'centro_formacion': 'Centro de Gestion Industrial',
        'regional': 'Distrito Capital',
        'fecha_creacion': '2023-03-10',
    },
]

programas = []
for prog_data in programas_data:
    prog = Programa.objects.create(**prog_data)
    programas.append(prog)
    print(f"✓ Creado programa: {prog.nombre}")

# ========== CREAR INSTRUCTORES ==========
print("\nCreando Instructores...")
instructores_data = [
    {
        'tipo_documento': 'CC',
        'numero_documento': '1010123456',
        'nombre': 'Andres',
        'apellido': 'Mendoza',
        'fecha_nacimiento': '1985-05-15',
        'telefono': '3001234567',
        'correo': 'andres.mendoza@sena.edu.co',
        'ciudad': 'Bogotá',
        'direccion': 'Cra 11 # 45-20',
        'nivel_educativo': 'ESP',
        'especialidad': 'Arquitectura de Software',
        'anos_experiencia': 8,
        'fecha_vinculacion': '2020-03-01',
    },
    {
        'tipo_documento': 'CC',
        'numero_documento': '1010654321',
        'nombre': 'Natalia',
        'apellido': 'Rojas',
        'fecha_nacimiento': '1988-08-22',
        'telefono': '3009876543',
        'correo': 'natalia.rojas@sena.edu.co',
        'ciudad': 'Bogotá',
        'direccion': 'Calle 72 # 18-30',
        'nivel_educativo': 'MAE',
        'especialidad': 'Ciberseguridad',
        'anos_experiencia': 10,
        'fecha_vinculacion': '2019-06-15',
    },
    {
        'tipo_documento': 'CC',
        'numero_documento': '1010789456',
        'nombre': 'Felipe',
        'apellido': 'Santos',
        'fecha_nacimiento': '1982-12-30',
        'telefono': '3005555555',
        'correo': 'felipe.santos@sena.edu.co',
        'ciudad': 'Bogotá',
        'direccion': 'Av 68 # 40-12',
        'nivel_educativo': 'TGL',
        'especialidad': 'Infraestructura TI',
        'anos_experiencia': 12,
        'fecha_vinculacion': '2018-01-10',
    },
]

instructores = []
for inst_data in instructores_data:
    inst = Instructor.objects.create(**inst_data)
    instructores.append(inst)
    print(f"✓ Creado instructor: {inst.nombre_completo()}")

# ========== CREAR CURSOS ==========
print("\nCreando Cursos...")
cursos_data = [
    {
        'codigo': 'ADSO-2025-01',
        'nombre': 'Software Empresarial - Cohorte 2025-01',
        'programa': programas[0],
        'instructor_coordinador': instructores[0],
        'fecha_inicio': '2025-01-10',
        'fecha_fin': '2027-01-10',
        'horario': 'Lunes a Viernes 08:00 - 12:00 y 14:00 - 18:00',
        'aula': 'Aula 101',
        'cupos_maximos': 30,
        'estado': 'INI',
    },
    {
        'codigo': 'SIGA-2025-02',
        'nombre': 'Seguridad Aplicada - Cohorte 2025-02',
        'programa': programas[1],
        'instructor_coordinador': instructores[1],
        'fecha_inicio': '2025-02-03',
        'fecha_fin': '2026-08-03',
        'horario': 'Lunes a Viernes 08:00 - 12:00',
        'aula': 'Aula 205',
        'cupos_maximos': 25,
        'estado': 'PRO',
    },
    {
        'codigo': 'ADTI-2024-03',
        'nombre': 'Sistemas Integrales - Cohorte 2024-03',
        'programa': programas[2],
        'instructor_coordinador': instructores[2],
        'fecha_inicio': '2024-09-15',
        'fecha_fin': '2026-09-15',
        'horario': 'Martes y Jueves 18:00 - 21:00',
        'aula': 'Virtual',
        'cupos_maximos': 35,
        'estado': 'EJE',
    },
]

cursos = []
for curso_data in cursos_data:
    curso = Curso.objects.create(**curso_data)
    cursos.append(curso)
    print(f"✓ Creado curso: {curso.nombre}")

# ========== CREAR APRENDICES ==========
print("\nCreando Aprendices...")
nombres = ['Brayan', 'Daniela', 'Kevin', 'Paula', 'Santiago', 'Manuela', 'Sebastian', 'Laura', 'Andres', 'Tatiana', 
           'Nicolas', 'Valeria', 'Mateo', 'Juliana', 'Camilo']
apellidos = ['Ruiz', 'Torres', 'Vargas', 'Castro', 'Herrera', 'Molina', 'Navarro', 'Salazar', 'Ortega', 'Pardo']
ciudades = ['Bogota', 'Medellin', 'Cali', 'Barranquilla', 'Bucaramanga', 'Pereira', 'Ibague', 'Neiva']

aprendices_data = []
for i in range(20):
    aprendiz_data = {
        'documento_identidad': f'1001{100000 + i}',
        'nombre': choice(nombres),
        'apellido': choice(apellidos),
        'telefono': f'300{randint(1000000, 9999999)}',
        'fecha_nacimiento': f'{randint(2003, 2007)}-{randint(1,12):02d}-{randint(1,28):02d}',
        'correo_electronico': f'grupo2026.aprendiz{i}@sena.edu.co',
        'ciudad': choice(ciudades),
        'programa': choice(programas).nombre,
    }
    aprendices_data.append(aprendiz_data)

# Crear aprendices en lotes
aprendices = []
for aprendiz_data in aprendices_data:
    aprendiz = Aprendiz.objects.create(**aprendiz_data)
    aprendices.append(aprendiz)

print(f"✓ Creados {len(aprendices)} aprendices")

# ========== ASIGNAR APRENDICES A CURSOS ==========
print("\nAsignando aprendices a cursos...")
for i, aprendiz in enumerate(aprendices):
    # Asignar aprendices al primer curso (ADSO)
    if i < 15:
        AprendizCurso.objects.create(
            aprendiz=aprendiz,
            curso=cursos[0],
            fecha_inscripcion='2025-01-05',
            estado='INS',
        )
    # Asignar aprendices al segundo curso (SIGA)
    if 8 <= i < 18:
        AprendizCurso.objects.create(
            aprendiz=aprendiz,
            curso=cursos[1],
            fecha_inscripcion='2025-01-28',
            estado='INS',
        )
    # Asignar aprendices al tercer curso (ADTI)
    if i < 20:
        AprendizCurso.objects.create(
            aprendiz=aprendiz,
            curso=cursos[2],
            fecha_inscripcion='2024-09-01',
            estado='AC',
        )

print("✓ Asignaciones completadas")

# ========== ASIGNAR INSTRUCTORES A CURSOS ==========
print("\nAsignando instructores a cursos...")
# Curso 1: Juan (coordinador) + María
InstructorCurso.objects.create(
    instructor=instructores[1],
    curso=cursos[0],
    rol='Instructor Teórico'
)

# Curso 2: María (coordinadora) + Carlos
InstructorCurso.objects.create(
    instructor=instructores[2],
    curso=cursos[1],
    rol='Instructor Práctico'
)

# Curso 3: Carlos (coordinador) + Juan
InstructorCurso.objects.create(
    instructor=instructores[0],
    curso=cursos[2],
    rol='Instructor Virtual'
)

print("✓ Instructores asignados")

# ========== RESUMEN ==========
print("\n" + "="*50)
print("DATOS CARGADOS EXITOSAMENTE")
print("="*50)
print(f"✓ {Programa.objects.count()} Programas")
print(f"✓ {Instructor.objects.count()} Instructores")
print(f"✓ {Curso.objects.count()} Cursos")
print(f"✓ {Aprendiz.objects.count()} Aprendices")
print(f"✓ {AprendizCurso.objects.count()} Inscripciones de Aprendices")
print(f"✓ {InstructorCurso.objects.count()} Asignaciones de Instructores")
print("="*50)
