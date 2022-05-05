from rest_framework import serializers
from envioinfo_app.models import Info 

#serializer para la info view y manejo más rápido de los datos.
class InfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    municipio= serializers.CharField()
    estado = serializers.CharField()
    colonia = serializers.CharField()
    cp = serializers.CharField()
    
    def create(self, validated_data):
        return Info.objects.create(**validated_data)
    
    
    #actualizando los datos de cada municipio
    def update(self, instance, validated_data):
        instance.municipio = validated_data.get('municipio', instance.municipio)
        instance.estado = validated_data.get('estado', instance.estado)
        instance.colonia = validated_data.get('colonia', instance.colonia)
        instance.cp = validated_data.get('cp', instance.cp)
        instance.save()
        return instance