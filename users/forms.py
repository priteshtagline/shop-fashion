from django import forms
from django.contrib.auth.forms import UserCreationForm as SignupFrom

from .models import User


class UserSignupForm(SignupFrom):
    """Signup form which displays email and password fields."""
    email = forms.EmailField(
        max_length=60, help_text='Required. Add a valid email address')

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
