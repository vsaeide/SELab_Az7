from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *


class UserRegisterForm(UserCreationForm):

    national_id=forms.CharField()
    type=forms.ChoiceField(choices =USER_TYPE)

    class Meta:
        model = User
        fields = ['username', 'national_id','type']

