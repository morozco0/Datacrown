from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('regiones',views.regiones,name="regiones"),
    path('medidas',views.medidas,name="medidas"),
    ##path('region',views.region,name='region')
]