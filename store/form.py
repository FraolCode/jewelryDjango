from dataclasses import field, fields
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm

from .models import User,Profile
from django import forms

class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter username' } ) )
    email = forms.CharField(widget=forms.TextInput(attrs={ 'class':'form-control', 'placeholder':'Enter Email' } ) )
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control js-child-focus js-visible-password','name':"password",'placeholder':'Password','pattern':".{5,}" } ) )
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control js-child-focus js-visible-password','name':"password",'placeholder':'Confirm Password','pattern':".{5,}" } ) )
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter username'  } ) )
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter firstname'   } ) )
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter firstname' } ) )
    email = forms.CharField(widget=forms.TextInput(attrs={ 'class':'form-control', 'placeholder':'Enter Email' } ) )
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email']

