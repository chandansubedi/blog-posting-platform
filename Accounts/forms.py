from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class signUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(signUpForm,self).__init__(*args, **kwargs)   

        for fieldname in ['username','email','password1','password2']:
            self.fields[fieldname].help_text = None

            