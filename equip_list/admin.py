from django.contrib import admin

from .models import Category,Machine,MachineImages
# Register your models here.

class MachineImagesAdmin(admin.StackedInline):
    model = MachineImages

    max_num = 3



class MachineAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'category', 'created_at','created_by']
    fieldsets = [
        (
            None, 
                  {"fields":["name",("price","year"),"description",'created_by']},
                  ),
                  ("Images",
                      {
                          "fields":['mainImage'],
                       },
                  )
                  ]

    inlines = [MachineImagesAdmin]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Machine,MachineAdmin)