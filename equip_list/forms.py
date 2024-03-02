from django import forms
from .models import Machine,MachineImages


class MachineForm (forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({'placeholder': 'Ej. 210H CAT','style': 'width:50%'})
        self.fields["name"].label = 'Nombre'
        self.fields["price"].widget.attrs.update({'placeholder': 'Ej. $10000','style': 'width:50%'})
        self.fields["price"].label = 'Precio'
        self.fields["year"].widget.attrs.update({'placeholder': 'Ej. 2002','style': 'width:50%'})
        self.fields["year"].label = 'Año'
        self.fields["mainImage"].widget.attrs.update({'style': 'width:50%, margin-left:auto'})
        self.fields["mainImage"].label = 'Imagen Principal'
        self.fields["category"].widget.attrs.update({'style': 'width:50%'})
        self.fields["category"].label = 'Categoria'
        self.fields['category'].initial = 'Select an option'
        self.fields["description"].widget.attrs.update({'style': 'width:50%'})
        self.fields["description"].label = 'Descripcion'



    class Meta:
        model = Machine
        fields = ('name','price','year','category','mainImage','description',)

class MachineImageForm(forms.ModelForm):

    class Meta:
        model = MachineImages
        fields = ('image',)
        exclude =['machine',]
        

