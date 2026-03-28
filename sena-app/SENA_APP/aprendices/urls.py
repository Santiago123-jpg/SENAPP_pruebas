from django.urls import path
from . import views

app_name = 'aprendices'

urlpatterns = [
    path('', views.main, name='main'),
    path('aprendices/', views.AprendizListView.as_view(), name='lista_aprendices'),
    path('aprendices/crear/', views.AprendizCreateView.as_view(), name='crear_aprendiz'),
    path('aprendices/<int:aprendiz_id>/', views.AprendizDetailView.as_view(), name='detalle_aprendiz'),
    path('aprendices/<int:aprendiz_id>/editar/', views.AprendizUpdateView.as_view(), name='editar_aprendiz'),
    path('aprendices/<int:aprendiz_id>/eliminar/', views.AprendizDeleteView.as_view(), name='eliminar_aprendiz'),
]