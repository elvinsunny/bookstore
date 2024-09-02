# products/forms.py

from django import forms
from . models import User

from django.contrib.auth.forms import UserCreationForm

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']