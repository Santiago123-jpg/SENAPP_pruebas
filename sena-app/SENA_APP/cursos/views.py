from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Curso
from django.views import generic
from django.urls import reverse_lazy
from .forms import CursoForm
from django.contrib import messages

# Create your views here.

def cursos(request):
    lista_cursos = Curso.objects.all()
    template = loader.get_template("lista_cursos.html")
    context = {
        "lista_cursos": lista_cursos,
    }
    return HttpResponse(template.render(context, request))


def detalle_curso(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    template = loader.get_template("detalle_cursos.html")
    # calcular cupos disponibles y ocupacion si se desea
    try:
        cupos_disponibles = curso.cupos_maximos - curso.aprendices.count()
    except Exception:
        cupos_disponibles = None

    context = {
        "curso": curso,
        "cupos_disponibles": cupos_disponibles,
        "instructores_count": curso.instructores.count() if hasattr(curso, 'instructores') else 0,
        "aprendices_count": curso.aprendices.count() if hasattr(curso, 'aprendices') else 0,
    }
    return HttpResponse(template.render(context, request))


class CursoCreateView(generic.CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'agregar_curso.html'
    success_url = reverse_lazy('cursos:lista_cursos')

    def form_valid(self, form):
        messages.success(self.request, f'Curso {form.instance.nombre} creado correctamente.')
        return super().form_valid(form)


class CursoUpdateView(generic.UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'editar_curso.html'
    pk_url_kwarg = 'curso_id'

    def get_success_url(self):
        return reverse_lazy('cursos:detalle_cursos', kwargs={'curso_id': self.object.pk})

    def form_valid(self, form):
        messages.success(self.request, f'Curso {form.instance.nombre} actualizado correctamente.')
        return super().form_valid(form)


class CursoDeleteView(generic.DeleteView):
    model = Curso
    template_name = 'eliminar_curso.html'
    pk_url_kwarg = 'curso_id'
    success_url = reverse_lazy('cursos:lista_cursos')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(request, f'Curso {obj.nombre} eliminado correctamente.')
        return super().delete(request, *args, **kwargs)
