from django.views.generic import CreateView, TemplateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserSignupForm, UserPersonalInfoChnageForm, UserPasswordChnageForm, UserEmailChnageForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import User



class UserSignUpView(CreateView):
    """This view is for the sign up page which displays signup form.
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
            return HttpResponseRedirect(self.get_success_url())


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    login_url = 'user:login'
    template_name = 'profile.html'
    
    def get_context_data(self, **kwargs):
        kwargs['personal_info_change_form'] = UserPersonalInfoChnageForm()
        kwargs['password_change_form'] = UserPasswordChnageForm(self.request.user)
        kwargs['email_change_form'] = UserEmailChnageForm(self.request.user)
        return kwargs
            
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())
    
    def post(self, request, *args, **kwargs):
        if 'personal_info_change_form' in request.POST:
            personal_info_change_form = UserPersonalInfoChnageForm(request.POST)
            if personal_info_change_form.is_valid():
                request.user.first_name = request.POST['first_name']
                request.user.last_name = request.POST['last_name']
                request.user.save()
            else:
                return JsonResponse({'form': False, 'errors': personal_info_change_form.errors})

        elif 'password_change_form' in request.POST:
            password_change_form = UserPasswordChnageForm(request.user, request.POST)
            if password_change_form.is_valid():
                self.request.user.set_password(request.POST['new_password'])
                self.request.user.save()
            else:
                return JsonResponse({'form': False, 'errors': password_change_form.errors})

        else:
            email_change_form = UserEmailChnageForm(request.user, request.POST)
            if email_change_form.is_valid():
                self.request.user.email = request.POST['new_email']
                self.request.user.save()
            else:
                ctxt['email_change_form'] = email_change_form

        return render(request, self.template_name, self.get_context_data(**ctxt))
