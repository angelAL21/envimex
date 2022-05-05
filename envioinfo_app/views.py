from django.shortcuts import render
from envioinfo_app.models import Info 
from django.http import JsonResponse

# el codigo ha sido comentado, fue credao para prueba del framework. 
# 
# mostrando todos los municipios que hay en la bd.
# def info_list(request):
#     municipios = Info.objects.all()
#     #reponse en forma de dic.
#     data= {
#      'municipios':list(municipios.values()),   
#     }
#     return JsonResponse(data)

# #obteniendo todos los datos de un municipio en especifico con ID.
# def municipio_detail(request, pk):
#     municipio = Info.objects.get(pk=pk)
#     data ={
#         'municipio': municipio.municipio,
#         'estado': municipio.estado,
#         'colonia': municipio.colonia,
#         'cp': municipio.cp
#     }
#     return JsonResponse(data)