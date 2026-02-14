from django.urls import path
from . import views

app_name = 'morfosintaxis'

urlpatterns = [
    path('', views.index, name='index'),
    path('lecciones/', views.lista_lecciones, name='lista_lecciones'),
    path('leccion/<int:numero>/', views.leccion_detalle, name='leccion_detalle'),
]
