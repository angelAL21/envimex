
from django.urls import path
from envioinfo_app.views import info_list, municipio_detail

#url para mostrar el lsitado de los municipios.
urlpatterns = [
    path('listado/', info_list, name='municipio-listado'),
    path('<int:pk>', municipio_detail, name='municipio-detalle'),
]
