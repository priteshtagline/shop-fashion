from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from .forms import UserSignupForm, UserPersonalInfoChnageForm, UserPasswordChnageForm, UserEmailChnageForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView


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
            return HttpResponseRedirect(self.get_success_url())


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    """This view is for the user profile page which displays email, password and personal info chnage form.
    The view extend for TempletView django metohd then three form pass in single profile templet and render to html.
    Post method in check wiche form fill by user then perfome oprtaion and apropriate change to user profile data
    and send response.
    """
    login_url = 'user:login'
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        kwargs['personal_info_change_form'] = UserPersonalInfoChnageForm(
            user, initial={'first_name': user.first_name, 'last_name': user.last_name})
        kwargs['password_change_form'] = UserPasswordChnageForm(user)
        kwargs['email_change_form'] = UserEmailChnageForm(user)
        return kwargs

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        form_data = request.POST
        user = self.request.user
        if 'first_name' in form_data and 'last_name' in form_data:
            personal_info_change_form = UserPersonalInfoChnageForm(
                user, form_data)
            if personal_info_change_form.is_valid():
                personal_info_change_form.save()
            else:
                return JsonResponse({'status': False, 'errors': personal_info_change_form.errors}, status=200)

        elif 'new_password' in form_data and 'current_password' in form_data:
            password_change_form = UserPasswordChnageForm(user, form_data)
            if password_change_form.is_valid():
                password_change_form.save()
                update_session_auth_hash(request, user)
            else:
                return JsonResponse({'status': False, 'errors': password_change_form.errors}, status=200)

        else:
            email_change_form = UserEmailChnageForm(user, form_data)
            if email_change_form.is_valid():
                email_change_form.save()
            else:
                return JsonResponse({'status': False, 'errors': email_change_form.errors}, status=200)

        return JsonResponse({'status': True, 'errors': ''}, status=200)
