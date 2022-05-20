from . import views
from django.urls import path

urlpatterns = [
    path("cursos",views.familiares),
    path("altaDeFamiliar/<nombre>/<int:dni>/<fechaDeNacimiento>/",views.altaDeFamiliar),
    path("listadoDeFamiliar",views.plantillaPrincipal)
]

