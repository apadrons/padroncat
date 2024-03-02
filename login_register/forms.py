from django import forms

from django.contrib.auth.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name','last_name','email','username')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({'placeholder': 'Nombre','style': 'width:50%'})
        self.fields["first_name"].label = 'Nombre'
        self.fields["last_name"].widget.attrs.update({'placeholder': 'Apellido','style': 'width:50%'})
        self.fields["last_name"].label = 'Apellido'
        self.fields["email"].widget.attrs.update({'placeholder': 'Correo electronico','style': 'width:50%'})
        self.fields["email"].label = 'Correo Electronico'
        self.fields["username"].widget.attrs.update({'placeholder': 'Nombre de usuario','style': 'width:50%'})
        self.fields["username"].label = 'Nombre de Usuario'
  


class LoginForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('username','password')