from django import forms
from django.contrib.auth.forms import UserCreationForm as SignupFrom

from .models import User


class UserSignupForm(SignupFrom):
    """Signup form which displays email and password fields."""
    class Meta(SignupFrom.Meta):
        widgets = {
            'gender': forms.RadioSelect()
        }
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'gender', 'phone_number')
