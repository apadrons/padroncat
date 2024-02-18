from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def index(request):
    return render(request,"core/index.html")

def about_view(request):
    return render(request,"core/nosotros.html")

def contact_view(request):
    return render(request,"core/contacto.html")