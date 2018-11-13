from django.urls import path
from . import views
from apps.mascota.views import mascota_view

urlpatterns = [
     path('', views.index, name='mascota'),
      path('', views.mascota_view, name='mascota_crear'),
]

