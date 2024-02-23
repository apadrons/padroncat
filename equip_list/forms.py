from django import forms


class MachineForm (forms.Form):
    name = forms.CharField(max_length=255,label='Machine Name: ')
    price = forms.IntegerField(label='Machine Price: ')
    year = forms.IntegerField(label='Machine Year: ')
    mainImage = forms.ImageField(label='Machine Main Image: ')
    description = forms.CharField(widget=forms.Textarea)

class MachineImages (forms.Form):
    image = forms.ImageField(label='Secondary Machine Image: ')