from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('name',)

    def __str__(self):
        return self.name
    

    
    
class Machine(models.Model):
    category= models.ForeignKey(Category,related_name = 'Machine',on_delete = models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    year = models.IntegerField()
    created_at =models.DateField(auto_now_add = True )
    created_by = models.ForeignKey(User,related_name = 'Machine',on_delete = models.CASCADE)
    mainImage = models.ImageField(upload_to='machine_images/', default='boo.png' , null=True)
    description = models.TextField(max_length=255,blank=True)


    def __str__(self):
        return self.name
    
    
class MachineImages(models.Model):
    image = models.ImageField(upload_to='machine_images/',null=True)
    machine = models.ForeignKey(Machine,on_delete = models.CASCADE)

    def save(self,*args,**kwargs):
        if self.id == None:
            if MachineImages.objects.filter(machine = self.machine).count() >= 3:
                print('issue')
        
        return super(MachineImages,self).save(*args,**kwargs)

    class Meta:
        verbose_name_plural = 'MachineImages'
    
    def __str__(self) -> str:
        return self.machine.name
    





