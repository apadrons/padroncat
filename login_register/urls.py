from django.urls import path
from . import views
# Create your views here.
from . import views

app_name='login_register'
urlpatterns = [ 
    
    path("register/",views.register_view, name='register'),
    path('login/',views.login_view,name='login'),
    path('test/',views.test_view,name='test'),
    path('logout/',views.logout_view,name='logout'),

    ]