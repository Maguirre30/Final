from django.urls import path
from Tienda import views

urlpatterns = [
    path('', views.index, name='index'),
    path('filtro_secciones/<int:seccion_id>', views.filtro_secciones, name="filtro_secciones"),
    path('registro/', views.registro, name='registro'),
]
