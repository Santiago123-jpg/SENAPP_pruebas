from django.test import TestCase
from django.http import Http404
from django.test import RequestFactory
from django.urls import reverse

from .forms import InstructorForm
from .models import Instructor
from .views import detalle_instructor, instructores, main


def instructor_data(**overrides):
	data = {
		"tipo_documento": "CC",
		"numero_documento": "2000000001",
		"nombre": "Diana",
		"apellido": "Suarez",
		"fecha_nacimiento": "1988-02-12",
		"telefono": "3002223344",
		"correo": "diana.suarez@example.com",
		"ciudad": "Bogota",
		"direccion": "Calle 10 # 20-30",
		"nivel_educativo": "ESP",
		"especialidad": "Desarrollo Web",
		"anos_experiencia": 7,
		"activo": True,
		"fecha_vinculacion": "2021-01-10",
	}
	data.update(overrides)
	return data


class InstructorModelTests(TestCase):
    # 1ra prueba
	def test_nombre_completo_y_str(self):
		instructor = Instructor.objects.create(**instructor_data())
		self.assertEqual(instructor.nombre_completo(), "Diana Suarez")
		self.assertEqual(str(instructor), "Diana Suarez - Desarrollo Web")


class InstructorFormTests(TestCase):
    # 2da prueba
	def test_form_rechaza_documento_no_numerico(self):
		form = InstructorForm(data=instructor_data(numero_documento="ABC123", correo="doc.invalido@example.com"))
		self.assertFalse(form.is_valid())
		self.assertIn("numero_documento", form.errors)

    # 3ra prueba
	def test_form_rechaza_telefono_no_numerico(self):
		form = InstructorForm(data=instructor_data(numero_documento="2000000002", telefono="300-ABCD", correo="tel.invalido@example.com"))
		self.assertFalse(form.is_valid())
		self.assertIn("telefono", form.errors)

    # 4ta prueba
	def test_form_valido(self):
		form = InstructorForm(data=instructor_data(numero_documento="2000000003", correo="valido@example.com"))
		self.assertTrue(form.is_valid())


class InstructorViewTests(TestCase):
	def setUp(self):
		self.factory = RequestFactory()
		self.instructor = Instructor.objects.create(**instructor_data())

    # 5ta prueba
	def test_main_view_responde_200(self):
		request = self.factory.get("/")
		response = main(request)
		self.assertEqual(response.status_code, 200)

    # 6ta prueba
	def test_lista_instructores_muestra_total(self):
		request = self.factory.get("/instructores/")
		response = instructores(request)
		self.assertEqual(response.status_code, 200)
		self.assertIn("Diana", response.content.decode("utf-8"))

    # 7ma prueba
	def test_detalle_instructor_por_ruta_nueva(self):
		request = self.factory.get(f"/instructores/{self.instructor.id}/")
		response = detalle_instructor(request, instructor_id=self.instructor.id)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Diana")

    # 8va prueba
	def test_detalle_instructor_por_ruta_legacy(self):
		request = self.factory.get(f"/instructores/details/{self.instructor.id}/")
		response = detalle_instructor(request, id_instructor=self.instructor.id)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Suarez")

    # 9na prueba
	def test_detalle_instructor_inexistente_retorna_404(self):
		request = self.factory.get("/instructores/99999/")
		with self.assertRaises(Http404):
			detalle_instructor(request, instructor_id=99999)


class InstructorUrlTests(TestCase):
    # 10ma prueba
	def test_reverse_detalle_instructor(self):
		self.assertEqual(reverse("instructores:detalle_instructor", kwargs={"instructor_id": 5}), "/instructores/5/")
