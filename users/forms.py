from django.contrib.auth.forms import UserCreationForm as SignupFrom
from django import forms
from django.utils.translation import gettext as _

from .models import User


class UserSignupForm(SignupFrom):
    """
    A form that lets a user signup form.
    The form is extend form django auth UserCreationForm and customize to 
    remove password2 field in signup form.
    """
    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)
        del self.fields['password2']

    class Meta(SignupFrom.Meta):
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1')

class UserPersonalInfoChnageForm(forms.ModelForm):
    """
    A form that lets a user change their personl informattion like first name and last name.
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name',)

class UserEmailChnageForm(forms.Form):
    """
    A form that lets a user change set their email while checking for a change in the
    e-mail.
    """
    error_messages = {
        'email_mismatch': _("The two e-mail address fields do not match."),
        'email_inuse': _("This e-mail address cannot be used. Please select a different e-mail address."),
        'password_incorrect': _("Incorrect password."),
    }

    password = forms.CharField(widget=forms.PasswordInput,required=True)
    new_email = forms.EmailField(max_length=254,required=True)
    confirm_email = forms.EmailField(max_length=254,required=True)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(UserEmailChnageForm, self).__init__(*args, **kwargs)
        
    def clean_password(self):
        """
        Validates that the user password field is correct.
        """
        password = self.cleaned_data["password"]
        if not self.user.check_password(password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'], code='password_incorrect',)
        return password


    def clean_new_email(self):
        """
        Prevents an e-mail address that is already registered from being registered by a different user.
        """
        email = self.cleaned_data.get('new_email')
        if User.objects.filter(email=email).count() > 0:
            raise forms.ValidationError(
                self.error_messages['email_inuse'], code='email_inuse',)
        return email

    def clean_confirm_email(self):
        """
        Validates that the confirm e-mail address's match.
        """
        email = self.cleaned_data.get('new_email')
        confirm_email = self.cleaned_data.get('confirm_email')
        if email and confirm_email:
            if email != confirm_email:
                raise forms.ValidationError(
                    self.error_messages['email_mismatch'], code='email_mismatch',)
        return confirm_email

    def save(self, commit=True):
        self.user.email = self.cleaned_data["new_email"]
        if commit:
            self.user.save()
        return self.user

class UserPasswordChnageForm(forms.Form):
    error_messages = {
        'password_incorrect': _("Incorrect password."),
    }
    
    current_password = forms.CharField(widget=forms.PasswordInput, required=True)
    new_password = forms.CharField(widget=forms.PasswordInput, required=True)
    
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(UserPasswordChnageForm, self).__init__(*args, **kwargs)
    
    def clean_current_password(self):
        """
        Validates that the current password field is correct.
        """
        current_password = self.cleaned_data["current_password"]
        if not self.user.check_password(current_password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'], code='password_incorrect',)
        return current_password
