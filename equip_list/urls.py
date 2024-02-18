from django.urls import path

from . import views

app_name = "equips"
urlpatterns = [ 
    path("",views.inventory, name='inventory'),
    path("<int:machine_id>/",views.detail, name='detail'),
    ]