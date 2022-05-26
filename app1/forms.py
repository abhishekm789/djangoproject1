from attr import fields
from django import forms
from app1.models import Register
class RegisterForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8)
    Confirmpassword=forms.CharField(widget=forms.PasswordInput,max_length=8)
    class Meta():
        model=Register
        fields='__all__'
class LoginForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8)
    class Meta():
        model=Register
        fields=('Email','Password')
class UpdateForm(forms.ModelForm):
    class Meta():
        model=Register
        fields=('Name','Age','Place','Photo','Email')