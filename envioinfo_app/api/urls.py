from django.urls import path
from envioinfo_app.api.views import municipio_list, municipio_details

#url para mostrar el lsitado de los municipios.
urlpatterns = [
    path('listado/', municipio_list, name='municipio-listado'), #todos los municipios
    path('<int:pk>', municipio_details, name='municipio-detalle'), #municipio by id
    
]