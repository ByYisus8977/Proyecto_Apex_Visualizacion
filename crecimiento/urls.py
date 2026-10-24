from django.urls import path

from . import views

urlpatterns = [
    path("", views.tabla_crecimiento, name="tabla_crecimiento"),
]
