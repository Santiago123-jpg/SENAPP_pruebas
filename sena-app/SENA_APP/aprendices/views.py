from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Aprendiz
from instructores.models import Instructor
from programas.models import Programa
from cursos.models import Curso 
from .forms import AprendizForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages


def main(request):
    template = loader.get_template("main.html")
    context = {
        'total_aprendices': Aprendiz.objects.count(),
        'total_instructores': Instructor.objects.count(),
        'total_programas': Programa.objects.count(),
        'total_cursos': Curso.objects.count(),
        'cursos_activos': Curso.objects.filter(estado='EJE').count(),
    }
    
    return HttpResponse(template.render(context, request))


class AprendizListView(generic.ListView):
    """Vista para listar todos los aprendices"""
    model = Aprendiz
    template_name = 'lista_aprendices.html'
    context_object_name = 'lista_aprendices'
    paginate_by = 20


class AprendizDetailView(generic.DetailView):
    """Vista para mostrar el detalle de un aprendiz"""
    model = Aprendiz
    template_name = 'detalle_aprendiz.html'
    context_object_name = 'aprendiz'
    pk_url_kwarg = 'aprendiz_id'


class AprendizCreateView(generic.CreateView):
    """Vista para crear un nuevo aprendiz"""
    model = Aprendiz
    form_class = AprendizForm
    template_name = 'agregar_aprendiz.html'
    success_url = reverse_lazy('aprendices:lista_aprendices')
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al crear el aprendiz"""
        messages.success(
            self.request,
            f'El aprendiz {form.instance.nombre_completo()} ha sido registrado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


class AprendizUpdateView(generic.UpdateView):
    """Vista para actualizar un aprendiz existente"""
    model = Aprendiz
    form_class = AprendizForm
    template_name = 'editar_aprendiz.html'
    pk_url_kwarg = 'aprendiz_id'
    
    def get_success_url(self):
        """Redirigir al detalle después de actualizar"""
        return reverse_lazy('aprendices:detalle_aprendiz', kwargs={'aprendiz_id': self.object.pk})
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al actualizar"""
        messages.success(
            self.request,
            f'El aprendiz {form.instance.nombre_completo()} ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


class AprendizDeleteView(generic.DeleteView):
    """Vista para eliminar un aprendiz"""
    model = Aprendiz
    template_name = 'eliminar_aprendiz.html'
    success_url = reverse_lazy('aprendices:lista_aprendices')
    pk_url_kwarg = 'aprendiz_id'
    
    def delete(self, request, *args, **kwargs):
        """Mostrar mensaje de éxito al eliminar"""
        aprendiz = self.get_object()
        messages.success(
            request,
            f'El aprendiz {aprendiz.nombre_completo()} ha sido eliminado exitosamente.'
        )
        return super().delete(request, *args, **kwargs)