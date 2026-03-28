from django import forms
from .models import Programa


class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = [
            'codigo', 'nombre', 'nivel_formacion', 'modalidad', 'duracion_meses', 'duracion_horas',
            'descripcion', 'competencias', 'perfil_egreso', 'requisitos_ingreso', 'centro_formacion',
            'regional', 'estado', 'fecha_creacion',
        ]
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'nivel_formacion': forms.Select(attrs={'class': 'form-select'}),
            'modalidad': forms.Select(attrs={'class': 'form-select'}),
            'duracion_meses': forms.NumberInput(attrs={'class': 'form-control'}),
            'duracion_horas': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'competencias': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'perfil_egreso': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'requisitos_ingreso': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'centro_formacion': forms.TextInput(attrs={'class': 'form-control'}),
            'regional': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'fecha_creacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
