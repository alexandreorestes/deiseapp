from django.contrib import admin
from django.urls import path
from . import views 


urlpatterns = [
    path('inserir/', views.inserir_dados, name='inserir_dados'),
    path('sucesso/', views.pagina_de_sucesso, name='sucesso'),  # Definindo uma rota para a página de sucesso
    path('', views.home, name='home'),
    path('vendas/', views.listar_vendas, name='listar_vendas'),
]

