from envioinfo_app.models import Info 
from envioinfo_app.api.serializers import InfoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

#lista todos los municipios.
@api_view(['GET', 'POST'])
def municipio_list(request):
    
    if request.method == 'GET':
        infos = Info.objects.all() #toda la info de los municipios
        serializer = InfoSerializer(infos, many=True) #serializer de municipios
        return Response(serializer.data) 

    if request.method == 'POST': #para publicar datos
        serializer = InfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

#lista municipios by id.
@api_view(['GET', 'PUT', 'DELETE'])
def municipio_details(request, pk):
    
    if request.method == 'GET':
        try:
            municipio = Info.objects.get(pk=pk)
        except Info.DoesNotExist:
            return Response({'Error':'municipio no encontrado'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = InfoSerializer(municipio)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        municipio = Info.objects.get(pk=pk)
        serializer = InfoSerializer(municipio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE': #eliminando municipio
        municipio = Info.objects.get(pk=pk)
        municipio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)