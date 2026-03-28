from django.test import TestCase
from django.test import RequestFactory

from .forms import AprendizForm
from .models import Aprendiz
from .views import main


class AprendizModelAndFormTests(TestCase):
    def setUp(self):
        self.aprendiz = Aprendiz.objects.create(
            documento_identidad="1000000001",
            nombre="Laura",
            apellido="Quintero",
            telefono="3001234567",
            fecha_nacimiento="2004-05-11",
            correo_electronico="laura.quintero@example.com",
            ciudad="Bogota",
            programa="ADSO",
        )

    # 1ra prueba
    def test_nombre_completo_y_str(self):
        self.assertEqual(self.aprendiz.nombre_completo(), "Laura Quintero")
        self.assertEqual(str(self.aprendiz), "Laura Quintero")

    # 2da prueba
    def test_form_rechaza_documento_no_numerico(self):
        form = AprendizForm(
            data={
                "documento_identidad": "ABC123",
                "nombre": "Ana",
                "apellido": "Lopez",
                "telefono": "3001234567",
                "correo_electronico": "ana.lopez@example.com",
                "fecha_nacimiento": "2005-01-01",
                "ciudad": "Bogota",
                "programa": "SIGA",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("documento_identidad", form.errors)

    # 3ra prueba
    def test_form_rechaza_telefono_con_longitud_invalida(self):
        form = AprendizForm(
            data={
                "documento_identidad": "1000000002",
                "nombre": "Ana",
                "apellido": "Lopez",
                "telefono": "30012",
                "correo_electronico": "ana2.lopez@example.com",
                "fecha_nacimiento": "2005-01-01",
                "ciudad": "Bogota",
                "programa": "SIGA",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("telefono", form.errors)

    # 4ta prueba
    def test_form_rechaza_correo_duplicado(self):
        form = AprendizForm(
            data={
                "documento_identidad": "1000000003",
                "nombre": "Laura",
                "apellido": "Rincon",
                "telefono": "3001234567",
                "correo_electronico": "laura.quintero@example.com",
                "fecha_nacimiento": "2005-01-01",
                "ciudad": "Bogota",
                "programa": "ADSO",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("correo_electronico", form.errors)


class AprendizViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    # 5ta prueba
    def test_main_view_responde_200(self):
        request = self.factory.get("/")
        response = main(request)
        self.assertEqual(response.status_code, 200)
