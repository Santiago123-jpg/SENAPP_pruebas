from django.urls import path
from . import views

app_name = 'instructores'

urlpatterns = [
    path('', views.main, name='main'),
    path('instructores/', views.instructores, name='lista_instructores'),
    path('instructores/crear/', views.InstructorCreateView.as_view(), name='crear_instructor'),
    path('instructores/<int:instructor_id>/', views.detalle_instructor, name='detalle_instructor'),
    path('instructores/<int:instructor_id>/editar/', views.InstructorUpdateView.as_view(), name='editar_instructor'),
    path('instructores/<int:instructor_id>/eliminar/', views.InstructorDeleteView.as_view(), name='eliminar_instructor'),
    path('instructores/details/<int:id_instructor>/', views.detalle_instructor, name='detalle_instructor_old'),
]   
