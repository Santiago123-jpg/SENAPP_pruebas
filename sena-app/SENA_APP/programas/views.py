from django.http import HttpResponse
from django.template import loader
from .models import Programa
from django.views import generic
from django.urls import reverse_lazy
from .forms import ProgramaForm
from django.contrib import messages

# Create your views here.

def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render({}, request))

def programas(request):
    lista_programas = Programa.objects.all()
    template = loader.get_template("lista_programas.html")
    context = {
        "lista_programas": lista_programas,
    }
    return HttpResponse(template.render(context, request))


def detalle_programa(request, programa_id):
    programa = Programa.objects.get(id=programa_id)
    template = loader.get_template("detalle_programas.html")
    context = {
        "programa": programa,
    }
    return HttpResponse(template.render(context, request))


class ProgramaCreateView(generic.CreateView):
    model = Programa
    form_class = ProgramaForm
    template_name = 'agregar_programa.html'
    success_url = reverse_lazy('programas:lista_programas')

    def form_valid(self, form):
        messages.success(self.request, f'Programa {form.instance.nombre} creado correctamente.')
        return super().form_valid(form)


class ProgramaUpdateView(generic.UpdateView):
    model = Programa
    form_class = ProgramaForm
    template_name = 'editar_programa.html'
    pk_url_kwarg = 'programa_id'

    def get_success_url(self):
        return reverse_lazy('programas:detalle_programas', kwargs={'programa_id': self.object.pk})

    def form_valid(self, form):
        messages.success(self.request, f'Programa {form.instance.nombre} actualizado correctamente.')
        return super().form_valid(form)


class ProgramaDeleteView(generic.DeleteView):
    model = Programa
    template_name = 'eliminar_programa.html'
    pk_url_kwarg = 'programa_id'
    success_url = reverse_lazy('programas:lista_programas')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(request, f'Programa {obj.nombre} eliminado correctamente.')
        return super().delete(request, *args, **kwargs)