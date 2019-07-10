from django.urls import path

from app import views
from .views import *

urlpatterns = [
    path('comunidades/', ListaComunidadesView.as_view(), name="comunidades"),
    path('comunidades/<int:pk>', ListaComunidadesView.as_view()),

    path('gestores/', ListaGestorView.as_view(), name="gestores"),

    path('inscritos_comunidad/', ListaInscritoComunidadView.as_view(), name="inscritos_comunidad"),
]