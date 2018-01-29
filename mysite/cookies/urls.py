from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('controlador1/', views.controlador1, name='controlador1'),
    path('controlador2/', views.controlador2, name='controlador2'),
]
