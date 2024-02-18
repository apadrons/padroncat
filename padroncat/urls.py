"""
URL configuration for padroncat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from core.views import index,about_view,contact_view
from equip_list.views import detail



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('nosotros/',about_view, name='nosotros'),
    path('contacto/',contact_view,name='contacto'),
    path("<int:machine_id>/",detail, name='detail'),
    path("inventory/",include('equip_list.urls', "equips"))


] 
urlpatterns +=  static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)