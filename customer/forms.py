from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model=User
        fields=["first_name","username","email","password1","password2"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),




        }

class LoginForm(forms.Form):
    username=forms.CharField(max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))