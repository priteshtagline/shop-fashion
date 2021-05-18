from django import forms
from .models import MyUser
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    """
    Form for Registering new users 
    """
    email = forms.EmailField(max_length=60, help_text = 'Required. Add a valid email address')
    class Meta:
        model = MyUser
        fields = ('email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        """
        specifying styles to fields 
        """
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field in (self.fields['email'],self.fields['password1'],self.fields['password2']):
            field.widget.attrs.update({'class': 'form-control '})

