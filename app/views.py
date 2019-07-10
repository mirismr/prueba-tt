from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


from .models import ComunidadEnergetica
from .serializers import *


class ListaComunidadesView(APIView):
    def get(self, request):
        queryset = ComunidadEnergetica.objects.all()
        serializer_class = ComunidadSerializer(queryset, many=True)

        return Response(serializer_class.data)

    def post(self, request):
        serializer = ComunidadSerializer(data=request.data)


        if serializer.is_valid(raise_exception=True):
            comunidad_saved=serializer.save()
        return Response({"success": "Comunidad '{}' creada".format(comunidad_saved.nombre)})

    def put(self, request, pk):
        saved_comunidad = get_object_or_404(ComunidadEnergetica.objects.all(), pk=pk)
        data = request.data
        serializer = ComunidadSerializer(instance=saved_comunidad, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):

            saved_comunidad = serializer.save()
        return Response({"success": "Comunidad '{}' actualizada".format(saved_comunidad.nombre)})

    def delete(self, request, pk):
        article = get_object_or_404(ComunidadEnergetica.objects.all(), pk=pk)
        article.delete()
        return Response({"message": "Comunidad con identificador `{}` borrada".format(pk)}, status=204)

class ListaGestorView(APIView):
    def get(self, request):
        queryset = Gestor.objects.all()
        serializer_class = GestorSerializer(queryset, many=True)

        return Response(serializer_class.data)

    def post(self, request):
        serializer = GestorSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            comunidad_saved = serializer.save()
        return Response({"success": "Gestor '{}' creado".format(comunidad_saved.nombre)})

class ListaInscritoComunidadView(APIView):
    def get(self, request):
        queryset = InscritoComunidad.objects.all()
        serializer_class = InscritoComunidadSerializer(queryset, many=True)

        return Response(serializer_class.data)

    def post(self, request):
        serializer = InscritoComunidadSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            comunidad_saved = serializer.save()
        return Response({"success": "Gestor '{}' creado".format(comunidad_saved.nombre)})



