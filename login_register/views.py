from django.shortcuts import render,get_object_or_404,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import UserForm,LoginForm


def register_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        password = request.POST.get('password')
        print(password)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            print(user.password)
            context = {
                'user':user,
            }
            return render(request, 'login_register/succesful_register.html',context=context)
        
        else:

            # The form is not valid.
            for field, error in form.errors.items():
                print(field, error)
            return HttpResponse('ERROR')##NEEDS HTML
    
    else: 
        form = UserForm()
        context ={
            'form':form
        }
        return render(request,'login_register/register.html',context=context)

    

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        clave = request.POST['password']
        user = authenticate( username = username, password=clave)
        print(user)
        if user is not None:
                login(request,user)

                return redirect(reverse('equips:inventory'))
        else:
            return redirect(reverse('equips:login'))


    return render(request,'login_register/login.html')


def test_view(request):
    if request.user.is_authenticated:
        return HttpResponse('YES')
    else:
            
        return HttpResponse('NO')
    
@login_required
def logout_view(request):
    logout(request)

    login_url = reverse('login_register:login')
    return redirect(login_url)