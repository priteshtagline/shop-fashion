from django import forms
from django.utils.translation import gettext as _


class UserPasswordChnageForm(forms.Form):
    """
    A form that lets a user change set their password while checking for a change in the
    password.
    """

    error_messages = {
        'password_incorrect': _("Incorrect password."),
    }

    current_password = forms.CharField(
        widget=forms.PasswordInput, required=True)
    new_password = forms.CharField(widget=forms.PasswordInput, required=True)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(UserPasswordChnageForm, self).__init__(*args, **kwargs)

    def clean_current_password(self):
        """
        Validates that the user current password field is correct.
        """
        current_password = self.cleaned_data["current_password"]
        if not self.user.check_password(current_password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'], code='password_incorrect',)
        return current_password

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data["new_password"])
        if commit:
            self.user.save()
        return self.user
