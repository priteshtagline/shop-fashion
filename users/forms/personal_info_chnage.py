from django import forms
from users.models import User


class UserPersonalInfoChnageForm(forms.ModelForm):
    """
    A form that lets a user change their personl informattion like first name and last name.
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name',)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(UserPersonalInfoChnageForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        self.user.first_name = self.cleaned_data["first_name"]
        self.user.last_name = self.cleaned_data["last_name"]
        if commit:
            self.user.save()
        return self.user
