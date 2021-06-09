from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.shortcuts import render

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
        kwargs['personal_info_change_form'] = UserPersonalInfoChnageForm()
        kwargs['password_change_form'] = UserPasswordChnageForm()
        kwargs['email_change_form'] = UserEmailChnageForm(self.request.user)
        return kwargs
            
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())
    
    def post(self, request, *args, **kwargs):
        ctxt = {}
        if 'personal_info_change_form' in request.POST:
            personal_info_change_form = UserPersonalInfoChnageForm(request.POST)
            if personal_info_change_form.is_valid():
                print(personal_info_change_form)
            else:
                ctxt['personal_info_change_form'] = personal_info_change_form

        elif 'password_change_form' in request.POST:
            password_change_form = UserPasswordChnageForm(request.POST)
            if password_change_form.is_valid():
                print(request)
            else:
                ctxt['password_change_form'] = password_change_form
                
        else:
            email_change_form = UserEmailChnageForm(request.user, request.POST)
            print(email_change_form)
            if email_change_form.is_valid():
                print(email_change_form)
            else:
                ctxt['email_change_form'] = email_change_form

        return render(request, self.template_name, self.get_context_data(**ctxt))
