from django.urls import path
from .views import inicio, qsomos, gestion, crear, eliminar, modificar, productos, contactanos, carrito, registrar

urlpatterns=[ 
    path('', inicio, name="inicio"),

    path('gestion/', gestion, name="gestion"),

    path('qsomos/', qsomos, name="qsomos"),
    path('crear/', crear, name="crear"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('modificar/<id>', modificar, name="modificar"),
    path('registrar/', registrar, name="registrar"),
    path('productos/', productos, name="productos"),
    path('contactanos/', contactanos, name="contactanos"),
    path('carrito/', carrito, name="carrito"),
    
]