from django.urls import path
from . import views


app_name = 'main'


urlpatterns = [
    path("", views.main, name= "main"),
    path("mostrarteste/", views.mainteste, name="mizera"),
    path("linkimagem/", views.linkimagem, name= 'isso')
    
]


