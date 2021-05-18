from .models import MyUser
from django.contrib import messages
from django.contrib.auth import (authenticate, logout, login)
from django.shortcuts import (render, get_object_or_404, HttpResponse, redirect)
from .forms import (UserRegistrationForm,
                    UserAuthenticationForm, UserUpdateform)


def home(request):
    """
    Home View Renders base.html
    """
    return render(request, "userapp/base.html", {})


def registration_view(request):
    """
    Renders Registration Form 
    """
    context = {}
    if request.POST:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_pass = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_pass)
            login(request, account)
            messages.success(
                request, "You have been Registered as {}".format(request.user.username))
            return redirect('home')
        else:
            messages.error(request, "Please Correct Below Errors")
            context['registration_form'] = form
    else:
        form = UserRegistrationForm()
        context['registration_form'] = form
    return render(request, "userapp/register.html", context)


def logout_view(request):
    logout(request)
    messages.success(request, "Logged Out")
    return redirect('login')


def login_view(request):
    """
    Renders Login Form
    """
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("home")
    if request.POST:
        form = UserAuthenticationForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            messages.success(request, "Logged In")
            return redirect("home")
        else:
            messages.error(request, "Please Correct Below Errors")
    else:
        form = UserAuthenticationForm()
    context['login_form'] = form
    return render(request, "userapp/login.html", context)


def account_view(request):
    """
    Renders userprofile page "
    """
    if not request.user.is_authenticated:
        return redirect("login")
    context = {}
    if request.POST:
        form = UserUpdateform(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "profile Updated")
        else:
            messages.error(request, "Please Correct Below Errors")
    else:
        form = UserUpdateform(
            initial={
                'email': request.user.email,
            }
        )
    context['account_form'] = form

    return render(request, "userapp/userprofile.html", context)
