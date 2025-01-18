from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class CustomerForm(ModelForm):
    class Meta:
        model = UserProfile
        fields =  '__all__'
        exclude = ['user']


class ItemsForm(ModelForm):
     class Meta:
        model = Items
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class userProfileForm(ModelForm):
    class Meta:
        model=UserProfile
        fields = '__all__'

class orderForm(ModelForm):
    class Meta:
        model=Order
        fields='__all__'