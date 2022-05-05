from envioinfo_app.models import Info 
from envioinfo_app.api.serializers import InfoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

#lista todos los municipios.
@api_view()
def municipio_list(request):
    infos = Info.objects.all() #toda la info de los municipios
    serializer = InfoSerializer(infos, many=True) #serializer de municipios
    return Response(serializer.data) 


#lista municipios by id.
@api_view()
def municipio_details(request, pk):
    municipio = Info.objects.get(pk=pk)
    serializer = InfoSerializer(municipio)
    return Response(serializer.data)