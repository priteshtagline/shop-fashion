from django.urls import include, path
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.UserSignUpView.as_view(), name="signup"),
    path('profile/', TemplateView.as_view(template_name='profile.html'), name="profile")
]


