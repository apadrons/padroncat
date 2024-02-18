from django.urls import path

from . import views


app_name = 'core'
urlpatterns = [ path("",views.index, name='index'),
               path("",views.about_view, name='nosotros'),
               path('',views.contact_view, name='contacto')]