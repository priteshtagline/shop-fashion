from django.views.generic import CreateView, DetailView
from .forms import UserSignupForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .models import User


class UserSignUpView(CreateView):
    """This view is for the sign up page which displays signup form.
    After successful registration, it will automatically login the user in the system and
    redirect user to the home page.
    """
    form_class = UserSignupForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'
    success_message = "Your profile was created successfully"
    
    def form_valid(self, form):
        super(UserSignUpView, self).form_valid(form)
        user = authenticate(
            self.request, email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
        if user:
            login(self.request, user)
            return HttpResponseRedirect(self.get_success_url())


