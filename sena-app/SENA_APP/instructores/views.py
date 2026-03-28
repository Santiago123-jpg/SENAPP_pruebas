from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Instructor
from django.views import generic
from django.urls import reverse_lazy
from .forms import InstructorForm
from django.contrib import messages


# Function view for main (kept for compatibility)
def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render({}, request))


def instructores(request):
    lista_instructores = Instructor.objects.all()
    template = loader.get_template("lista_instructores.html")
    
    context = {
        "lista_instructores": lista_instructores,
        'total_instructores': lista_instructores.count(),
    }
    return HttpResponse(template.render(context, request))


def detalle_instructor(request, instructor_id=None, id_instructor=None):
    # Accept either 'instructor_id' or 'id_instructor' from different URL patterns
    id_actual = instructor_id if instructor_id is not None else id_instructor
    instructor = get_object_or_404(Instructor, id=id_actual)
    template = loader.get_template('detalle_instructor.html')
    # gather related courses if available
    cursos_coordinados = instructor.cursos_coordinados.all() if hasattr(instructor, 'cursos_coordinados') else []
    cursos_impartidos = instructor.cursos_impartidos.all() if hasattr(instructor, 'cursos_impartidos') else []
    context = {
        'instructor': instructor,
        'cursos_coordinados': cursos_coordinados,
        'cursos_impartidos': cursos_impartidos,
    }
    return HttpResponse(template.render(context, request))


class InstructorCreateView(generic.CreateView):
    model = Instructor
    form_class = InstructorForm
    template_name = 'agregar_instructor.html'
    success_url = reverse_lazy('instructores:lista_instructores')

    def form_valid(self, form):
        messages.success(self.request, f'Instructor {form.instance.nombre} {form.instance.apellido} creado correctamente.')
        return super().form_valid(form)


class InstructorUpdateView(generic.UpdateView):
    model = Instructor
    form_class = InstructorForm
    template_name = 'editar_instructor.html'
    pk_url_kwarg = 'instructor_id'

    def get_success_url(self):
        return reverse_lazy('instructores:detalle_instructor', kwargs={'id_instructor': self.object.pk})

    def form_valid(self, form):
        messages.success(self.request, f'Instructor {form.instance.nombre} {form.instance.apellido} actualizado correctamente.')
        return super().form_valid(form)


class InstructorDeleteView(generic.DeleteView):
    model = Instructor
    template_name = 'eliminar_instructor.html'
    pk_url_kwarg = 'instructor_id'
    success_url = reverse_lazy('instructores:lista_instructores')

    def delete(self, request, *args, **kwargs):
        instructor = self.get_object()
        messages.success(request, f'Instructor {instructor.nombre} {instructor.apellido} eliminado correctamente.')
        return super().delete(request, *args, **kwargs)