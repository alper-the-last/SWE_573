from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SearchForm(forms.Form):
     # an input that is a chracter field
     q=forms.CharField(label='search')

class tagFunction(forms.Form):
    tag_term = forms.CharField(label='Tag')

class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']