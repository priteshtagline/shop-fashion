from django.contrib.auth.forms import UserCreationForm as SignupFrom

from .models import User


class UserSignupForm(SignupFrom):
    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)
        del self.fields['password2']

    class Meta(SignupFrom.Meta):
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1')

