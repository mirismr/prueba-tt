from rest_framework import serializers
from .models import *


class ComunidadSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField()
    descripcion = serializers.CharField()
    latitud = serializers.FloatField()
    longitud = serializers.FloatField()
    id_gestor = serializers.CharField()

    def create(self, validated_data):
            return ComunidadEnergetica.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.latitud = validated_data.get('latitud', instance.latitud)
        instance.longitud = validated_data.get('longitud', instance.longitud)
        instance.longitud = validated_data.get('longitud', instance.longitud)

        instance.save()
        return instance


class GestorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField()

    def create(self, validated_data):
            return Gestor.objects.create(**validated_data)


class InscritoComunidadSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    dni = serializers.CharField(max_length=10)
    nombre = serializers.CharField(max_length=200)
    apellidos = serializers.CharField(max_length=200)
    latitud_der = serializers.FloatField()
    longitud_der = serializers.FloatField()
    nombre_der = serializers.CharField(max_length=200)

    def create(self, validated_data):
            return InscritoComunidad.objects.create(**validated_data)

    def validate(self, data):
        queryset = ComunidadEnergetica.objects.all()

        distancias = []
        for comunidad in queryset:
            distancia = self.distance(comunidad.latitud, comunidad.longitud, data.latitud_der, data.longitud_der)

            distancias.append(distancia)

        distancia = min(distancias)

        if distancia > 500:
            raise serializers.ValidationError("La distancia entre la comunidad y el DER no puede ser superior a 500m")

        return data



    def distance(self, lat1, lon1, lat2, lon2):
        import math
        radius = 6371000  # metros

        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
             math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
             math.sin(dlon / 2) * math.sin(dlon / 2))
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = radius * c

        return d
