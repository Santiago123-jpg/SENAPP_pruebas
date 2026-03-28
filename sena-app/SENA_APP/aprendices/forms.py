from django import forms
from .models import Aprendiz


class AprendizForm(forms.ModelForm):
    """Formulario basado en modelo para crear y editar aprendices"""
    
    class Meta:
        model = Aprendiz
        fields = [
            'documento_identidad',
            'nombre',
            'apellido',
            'telefono',
            'correo_electronico',
            'fecha_nacimiento',
            'ciudad',
            'programa'
        ]
        # Widgets personalizados para mejorar la interfaz en el HTML
        widgets = {
            'documento_identidad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el documento'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre'
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el apellido'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '3001234567'
            }),
            'correo_electronico': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com'
            }),
            'programa': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del programa'
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'ciudad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ciudad de residencia'
            })
        }
        # Etiquetas personalizadas
        labels = {
            'documento_identidad': 'Documento de Identidad',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'telefono': 'Teléfono',
            'correo_electronico': 'Correo Electrónico',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'ciudad': 'Ciudad',
            'programa': 'Programa de Formación'
        }

    # Validaciones personalizadas
    
    def clean_documento_identidad(self):
        """Validar que el documento contenga solo números"""
        documento = self.cleaned_data.get('documento_identidad')
        if not documento.isdigit():
            raise forms.ValidationError("El documento debe contener solo números.")
        return documento

    def clean_telefono(self):
        """Validar que el teléfono contenga solo números"""
        telefono = self.cleaned_data.get('telefono')
        if telefono and not telefono.isdigit():
            raise forms.ValidationError("El teléfono debe contener solo números.")
        if telefono and len(telefono) != 10:
            raise forms.ValidationError("El teléfono debe tener 10 dígitos.")
        return telefono

    def clean_correo_electronico(self):
        """Validar que el correo sea único"""
        correo = self.cleaned_data.get('correo_electronico')
        if correo:
            # Excluir el actual si es una actualización
            qs = Aprendiz.objects.filter(correo_electronico=correo)
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise forms.ValidationError("Este correo electrónico ya está registrado.")
        return correo