from django import forms
from .models import MyUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
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


class UserAuthenticationForm(forms.ModelForm):
    """
    Form for Logging in  users
    """
    password  = forms.CharField(label= 'Password', widget=forms.PasswordInput)

    class Meta:
        model  =  MyUser
        fields =  ('email', 'password')
        widgets = {
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        """
        specifying styles to fields 
        """
        super(UserAuthenticationForm, self).__init__(*args, **kwargs)
        for field in (self.fields['email'],self.fields['password']):
            field.widget.attrs.update({'class': 'form-control '})

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid Login')


class UserUpdateform(forms.ModelForm):
    """
    Updating User Info
    """
    class Meta:
        model  = MyUser
        fields = ('email',)
        widgets = {
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        """
        specifying styles to fields 
        """
        super(UserUpdateform, self).__init__(*args, **kwargs)
        for field in (self.fields['email'],):
            field.widget.attrs.update({'class': 'form-control '})

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = MyUser.objects.exclude(pk = self.instance.pk).get(email=email)
            except MyUser.DoesNotExist:
                return email
            raise forms.ValidationError("Email '%s' already in use." %email)

