from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.forms import formset_factory
from .forms import MachineForm,MachineImageForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages



from .models import Machine,Category,MachineImages
# Create your views here.

def inventory(request):

    machines = Machine.objects.filter(approved=False) #Cleaning for approved machines only
    categories = Category.objects.all()

    context = {
        'categories': categories,
        'machines': machines,
    }

    return render(request,'equip_list/inventory.html',context=context)

def filtered_inventory(request,category_name):

    categoria = get_object_or_404(Category, name = category_name.capitalize())
    categories = Category.objects.all()
    machines = Machine.objects.filter(approved = False, category = categoria.id)

    context = {
        'categories': categories,
        'machines': machines,
    }
    return render(request,'equip_list/inventory.html',context=context)

'''------------DETAIL IMAGE------------'''

def detail(request,machine_id):

    machine = get_object_or_404(Machine,pk=machine_id)
    images = MachineImages.objects.filter(machine=machine)
    tempImages =[]
    for image in images:

        tempImages.append(image.image)
    print(tempImages)
    context = {
        'machine':machine,
        'images':tempImages,
    }
    return render(request,'equip_list/detail.html',context=context) 

'''------------END DETAIL IMAGE------------'''



'''------------NEW MACHINE------------'''

@login_required
def new_machine_intro(request):

    return render(request,'equip_list/intro_new_machine.html')

@login_required
def new_machine_view(request):
    
    ImageForm = formset_factory(MachineImageForm,extra=3)

    if request.method == "POST":
        form = MachineForm(request.POST, request.FILES,prefix='main')
        formset = ImageForm(request.POST,request.FILES,prefix= 'image')

        if form.is_valid():
            newMachine = form.save(commit=False)
            newMachine.created_by = request.user
            newMachine.save()

            if formset.is_valid():
                for form_1 in formset:
                    images = form_1.save(commit = False)
                    images.machine = newMachine
                    images.save()

            return  detail(request=request,machine_id=newMachine.id)
        
        else:
            imageForm = ImageForm(prefix='image')
            return render(request,'equip_list/new_machine.html',{
            'form':form,
            'imageForm':imageForm,
        }) 
            
    else:
        form = MachineForm(prefix='main')
        imageForm = ImageForm(prefix='image') 
        context={
            'form':form,
            'imageForm':imageForm,
        }

    return render(request,'equip_list/new_machine.html',context=context) 

'''------------END NEW MACHINE------------'''
@login_required
def user_inventory_view(request):

    machines = Machine.objects.filter(created_by = request.user)
    for machine in machines:
        print(machine.approved)
    context = {
        'machines':machines,
    }

    return render (request,'equip_list/user_inventory.html',context=context)