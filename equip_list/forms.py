from django import forms
from .models import Category,Machine


class MachineForm (forms.ModelForm):
    class Meta:
        model = Machine
        exclude = ['created_by','created_at','approved']

    # name = forms.CharField(max_length=255,label='Nombre de Maquina:', widget=forms.TextInput(attrs={'placeholder': 'Ej. 210H CAT',                                                                                                    'style': 'width:50%'}))
    # price = forms.IntegerField(label='Precio: ',
    #                            widget=forms.NumberInput(attrs={'placeholder': 'Ej. $10000',                                                                              'style': 'width:50%'}))
    # year = forms.IntegerField(label='Año: ',
    #                            widget=forms.NumberInput(attrs={'placeholder': 'Ej. 2002',                                                                              'style': 'width:50%'}))
    # category = forms.ModelChoiceField(queryset=Category.objects.all(),to_field_name = 'name', required=True, widget=forms.Select(attrs={'style': 'width:50%'}))
    # mainImage = forms.ImageField(label='Imagen Principal: ')
    # description = forms.CharField(label = 'Descripcion',
    #                            widget=forms.TextInput(attrs={'style': 'width:50%'}))

    # class Meta:
    #     model = Machine


class MachineImages (forms.Form):
    image = forms.ImageField(label='Secondary Machine Image: ')