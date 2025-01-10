from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_campistas, name='lista_campistas'),
    path('campistas/', views.lista_campistas, name='lista_campistas'),
    path('campistas/nuevo/', views.nuevo_campista, name='nuevo_campista'),
    path('campistas/<int:pk>/', views.detalle_campista, name='detalle_campista'),
    path('campistas/<int:pk>/editar/', views.editar_campista, name='editar_campista'),
    path('campistas/<int:pk>/eliminar/', views.eliminar_campista, name='eliminar_campista'),
    path('reservas/', views.lista_reservas, name='lista_reservas'),
    path('reservas/nueva/', views.nueva_reserva, name='nueva_reserva'),
    path('reservas/<int:pk>/', views.detalle_reserva, name='detalle_reserva'),
    path('reservas/<int:pk>/editar/', views.editar_reserva, name='editar_reserva'),
    path('reservas/<int:pk>/eliminar/', views.eliminar_reserva, name='eliminar_reserva'),
]
