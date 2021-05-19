from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm as SignupFrom


class UserSignupForm(SignupFrom):
    """
    UserCreattionForm extend as SignupFrom for django auth form.
    User model to create form and username field remove and add email field.
    """
    email = forms.EmailField(max_length=60, help_text = 'Required. Add a valid email address')
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

