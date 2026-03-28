from django import forms
from .models import Instructor


class InstructorForm(forms.ModelForm):
    """Formulario basado en modelo para crear y editar instructores"""
    
    class Meta:
        model = Instructor
        fields = [
            'numero_documento',
            'tipo_documento',
            'nombre',
            'apellido',
            'telefono',
            'correo',
            'fecha_nacimiento',
            'ciudad',
            'direccion',
            'nivel_educativo',
            'especialidad',
            'anos_experiencia',
            'activo',
            'fecha_vinculacion',
        ]
        widgets = {
            'documento_identidad': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_documento': forms.Select(attrs={'class': 'form-select'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'nivel_educativo': forms.Select(attrs={'class': 'form-select'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control'}),
            'anos_experiencia': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'fecha_vinculacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def clean_numero_documento(self):
        """Validar documento de identidad"""
        documento = self.cleaned_data.get('numero_documento')
        if not documento.isdigit():
            raise forms.ValidationError("El documento debe contener solo números.")
        return documento
    
    def clean_telefono(self):
        """Validar teléfono"""
        telefono = self.cleaned_data.get('telefono')
        if telefono and not telefono.isdigit():
            raise forms.ValidationError("El teléfono debe contener solo números.")
        return telefono