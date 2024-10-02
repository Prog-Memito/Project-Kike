from django import forms
from .models import Tilla, Serie
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError

# CREA EL FORMULARIO PARA PRODUCTOS

class TillaForm(forms.ModelForm):

    class Meta:
        model = Tilla
        fields = '__all__'

class UpdateTillaForm(forms.ModelForm):

    class Meta:
        model = Tilla
        fields = ['nombre','serie','descripcion','tp_producto','precio','foto']

# FROM PARA EL REGISTRO USUARIOS

class UserForm(UserCreationForm):
    username=forms.CharField(min_length=5,max_length=50)
    first_name=forms.CharField(min_length=3, max_length=50)
    last_name=forms.CharField(min_length=4, max_length=50)

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']

class UptadeUserForm(forms.ModelForm):
    username=forms.CharField(min_length=5,max_length=50)
    first_name=forms.CharField(min_length=3, max_length=50)
    last_name=forms.CharField(min_length=4, max_length=50)

    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

# FORM PARA REGISTRO SERIE
class SerieForm(forms.ModelForm):

    class Meta:
        model = Serie
        fields = '__all__'