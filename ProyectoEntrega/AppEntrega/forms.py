from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  
from AppEntrega.models import *
from django import forms
from .models import Comentario

class EstiloFormulario(forms.Form):
    estilo= forms.CharField()

class MagoFormulario(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()

class TrucoFormulario(forms.Form):
    nombre= forms.CharField() 
    clase= forms.CharField()

class BusquedaMago(forms.Form):
    nombre =  forms.CharField()

class MyUserCreationForm(UserCreationForm):

    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput)
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: '' for k in fields}

class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        field = '__all__'
        exclude = ['user']  

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nombre', 'texto']
        labels = {'nombre': 'Nombre', 'texto': 'Comentario'}
        widgets = {'nombre': forms.TextInput(attrs={'required': True}), 'texto': forms.Textarea(attrs={'required': True})}