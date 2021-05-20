from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from .forms import UserSignupForm


def signup_view(request):
    """This view is for the sign up page which displays signup form.
    After successful registration, it will automatically login the user in the system and
    redirect user to the home page.
    """
    context = {}
    if request.POST:
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=password)
            login(request, account)
            messages.success(
                request, "Thank you for signup.")
            return redirect('home')
        else:
            messages.error(request, "Please Correct Below Errors")
            context['signup_form'] = form
    else:
        form = UserSignupForm()
        context['signup_form'] = form
    return render(request, "signup.html", context)
