
from django.urls import path
from envioinfo_app.views import info_list

#url para mostrar el lsitado de los municipios.
urlpatterns = [
    path('listado/', info_list, name='municipio-listado'),
]
