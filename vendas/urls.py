from django.contrib import admin
from django.urls import path, include
from appvendas.views import inserir_dados, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('appvendas/', include('appvendas.urls')),  # Incluindo as URLs do aplicativo appvendas
    path('inserir', inserir_dados, name='inserir_dados' ),
]