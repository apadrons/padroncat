from django.shortcuts import render,get_object_or_404


from .models import Machine,Category,MachineImages
# Create your views here.

def inventory(request):

    machines = Machine.objects.all()
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