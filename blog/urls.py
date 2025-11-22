from django.urls import path
from . import views

urlpatterns = [
    path('', views.template_view, name='home'),  
    path('pruebas/', views.pruebas, name='pruebas'),
    path('template/', views.template_view, name='template'),
]
