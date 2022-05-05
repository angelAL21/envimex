from rest_framework import serializers

#serializer para la info view y manejo más rápido de los datos.
class InfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    municipio= serializers.CharField()
    estado = serializers.CharField()
    colonia = serializers.CharField()
    cp = serializers.CharField()