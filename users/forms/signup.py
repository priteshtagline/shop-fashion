from django.contrib.auth.forms import UserCreationForm as SignupFrom
from users.models import User


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
