from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm as SignupFrom


class UserSignupForm(SignupFrom):
    """
    Form for Registering new users 
    """
    email = forms.EmailField(max_length=60, help_text = 'Required. Add a valid email address')
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

