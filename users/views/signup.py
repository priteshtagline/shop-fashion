from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms.signup import UserSignupForm
from users.models import UserWishlist


class UserSignUpView(CreateView):
    """This view is for the sign up page which display signup form.
    If user is already login in website then user automatically redirect to home page 
    otherwise display signup form.
    After successful registration, it will automatically login the user in the system and
    redirect user to the home page.
    """

    form_class = UserSignupForm
    success_url = reverse_lazy('website:home')
    template_name = 'signup.html'
    success_message = "Your profile was created successfully"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return redirect('website:home')

    def form_valid(self, form):
        super(UserSignUpView, self).form_valid(form)
        user = authenticate(
            self.request, email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
        if user:
            login(self.request, user)
            UserWishlist.objects.create(user=user, name='wish list')
            return HttpResponseRedirect(self.get_success_url())
