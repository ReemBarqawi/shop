from django import forms
from .models import Product
from .models import Category

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class AdminSignUpForm(UserCreationForm):
    make_admin = forms.BooleanField(required=False, label="Sign up as Admin (temporary)")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'make_admin']