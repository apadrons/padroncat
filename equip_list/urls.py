from django.urls import path

from . import views

app_name = "equips"
urlpatterns = [ 
    
    path("",views.inventory, name='inventory'),
    path("<int:machine_id>/",views.detail, name='detail'),
    path("new_machine/intro", views.new_machine_intro, name='new_machine_intro'),
    path("new_machine/", views.new_machine_view, name='new_machine'),
    ]