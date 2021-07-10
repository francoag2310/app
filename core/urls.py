from django.urls import path
from core.sedes.views import *

urlpatterns = [
    path('', SedeListView.as_view(), name='sede_list_view'),
    path('CrearSede/', SedeCreateView.as_view(), name='sede_create_view'),
]
