from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect


from .models import Machine,Category,MachineImages,MachineForm,ImageForm
# Create your views here.

def inventory(request):

    
    machines = Machine.objects.filter(approved=True) #Cleaning for approved machines only
    categories = Category.objects.all()

    return render(request,'equip_list/inventory.html',{
        'categories': categories,
        'machines': machines,
    })


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


def new_machine_view(request):
    if request.method == "POST":
        form = MachineForm(request.POST)
        if form.is_valid():
            newMachine = form.save()
            newMachine_id = newMachine.id 
            return  detail(request=request,machine_id=newMachine_id)
    else:
        form = MachineForm()
        context = {
            "form":form,
        }
    return render(request,'equip_list/new_machine.html',context=context) 


