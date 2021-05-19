from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserSignupForm


def signup_view(request):
    """
    The user fill the signup form and submit. 
    If form data is validate then automaticaly user login and redirect to the website home page.
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
                request, "You have been signup as {}".format(request.user.email))
            return redirect('home')
        else:
            messages.error(request, "Please Correct Below Errors")
            context['signup_form'] = form
    else:
        form = UserSignupForm()
        context['signup_form'] = form
    return render(request, "signup.html", context)
