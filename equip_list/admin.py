from django.contrib import admin

from .models import Category,Machine,MachineImages
# Register your models here.

class MachineImagesAdmin(admin.StackedInline):
    model = MachineImages

class MachineAdmin(admin.ModelAdmin):
    list_display = ['name']

    inlines = [MachineImagesAdmin]



admin.site.register(Category)
admin.site.register(Machine,MachineAdmin)