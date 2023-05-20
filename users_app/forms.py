from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from .models import Users

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={
        "class" : "form-control py-4",
        "placeholder" : "write your username"
    }))
    password = forms.CharField(widget = forms.PasswordInput(attrs={
        "class" : "form-control py-4",
        "placeholder" : "write password"
    }))
    class Meta:
        model = Users
        fields = ("username", "password")

# -------------------------------------------------------------------------------------------------

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget = forms.TextInput(attrs={
        "class" : "form-control py-4",
        "placeholder" : "write your name"
    }))
    last_name = forms.CharField(widget = forms.TextInput(attrs={
        "class" : "form-control py-4",
        "placeholder" : "write your surename"
    }))
    username = forms.CharField(widget = forms.TextInput(attrs={
        "class" : "form-control py-4",
        "placeholder" : "write your username"
    }))
    email = forms.CharField(widget = forms.TextInput(attrs={
        "class" : "form-control py-4",
        "placeholder" : "write your email"
    }))
    password1 = forms.CharField(widget = forms.PasswordInput(attrs={
        "class" : "form-control py-4",
        "placeholder" : "write password"
    }))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={
        "class" : "form-control py-4",
        "placeholder" : "write password(again)"
    }))
    

    class Meta:
        model = Users
        fields = ("first_name", "last_name","username","email", "password1","password2")

# ---------------------------------------------------------------------------------------------------------------


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget = forms.TextInput(attrs={
        "class" : "form-control py-4",
        "placeholder" : "write your name"
    }))
    last_name = forms.CharField(widget = forms.TextInput(attrs={
        "class" : "form-control py-4",
        "placeholder" : "write your surename"
    }))
    image = forms.ImageField(widget= forms.FileInput(attrs={
        "class" : "custom-file-input"
        
    }), required=False)
    username = forms.CharField(widget = forms.TextInput(attrs={
        "class" : "form-control py-4",
        "placeholder" : "write your username",
        "readonly":True
    }))
    email = forms.CharField(widget = forms.TextInput(attrs={
        "class" : "form-control py-4",
        "placeholder" : "write your email",
        "readonly":True
    }))
    class Meta:
        model = Users
        fields = ("first_name", "last_name","image","username","email")


