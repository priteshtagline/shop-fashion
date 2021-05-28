from django.urls import include, path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('signup/', views.UserSignUpView.as_view(), name="signup"),
    path('account/', TemplateView.as_view(template_name='account.html'), name="account")
]
