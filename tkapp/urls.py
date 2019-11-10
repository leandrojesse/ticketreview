from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gerador', views.gerador, name='gerador'),
    path('listaservidores', views.listaservidores, name='listaservidores'),
]