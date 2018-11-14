from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
     path('', views.index, name='mascota'),
     path('nuevo', login_required(views.MascotaCreate.as_view()) , name='mascota_crear'),
     path('listar', login_required(views.MascotaList.as_view()), name='mascota_listar'),
	 path('editar/<int:pk>/', login_required(views.MascotaUpdate.as_view()),name='mascota_editar'),
	 path('deletiar/<int:pk>/', login_required(views.MascotaDelete.as_view()) ,name='mascota_eliminar'),

	]

