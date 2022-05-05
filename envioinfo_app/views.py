from django.shortcuts import render
from envioinfo_app.models import Info 
from django.http import JsonResponse

# mostrando todos los municipios que hay en la bd.
def info_list(request):
    municipios = Info.objects.all()
    #reponse en forma de dic.
    data= {
     'municipios':list(municipios.values()),   
    }
    return JsonResponse(data)