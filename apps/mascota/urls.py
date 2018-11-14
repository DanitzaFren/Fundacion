from django.urls import path
from . import views


urlpatterns = [
     path('', views.index, name='mascota'),
     path('nuevo', views.MascotaCreate.as_view(), name='mascota_crear'),
     path('listar', views.MascotaList.as_view(), name='mascota_listar'),
	 path('editar/<int:pk>/',views.MascotaUpdate.as_view(),name='mascota_editar'),
	 path('deletiar/<int:pk>/',views.MascotaDelete.as_view(),name='mascota_eliminar'),

	]

