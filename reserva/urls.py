from django.contrib import admin
from django.urls import path, include  # Importa 'include' para incluir las URLs de la aplicación

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el panel de administración
    path('', include('Aplicacion.Reserva.urls')),  # Asegúrate de que la ruta sea correcta
]
