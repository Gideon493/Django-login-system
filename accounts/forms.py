
from django import forms
from django.forms import ModelForm
from accounts.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'firstname', 'lastname', 'username', 'email', 'password'
        ]

