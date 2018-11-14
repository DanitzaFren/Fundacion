from django.urls import path
from . import views



urlpatterns = [
	path('index', views.index_adopcion, name='index'),
    path('listar', views.SolicitudList.as_view(), name='solicitud_listar'),
    path('nueva', views.SolicitudCreate.as_view(), name='solicitud_crear'),
     path('editar/<int:pk>/', views.SolicitudUpdate.as_view(), name='solicitud_editar'),
     path('eliminar/<int:pk>/', views.SolicitudDelete.as_view(), name='solicitud_eliminar'),
]