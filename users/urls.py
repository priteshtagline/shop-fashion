from django.contrib.auth import views as auth_views
from django.urls import include, path, reverse_lazy

from users.views.profile import ProfileUpdateView
from users.views.signup import UserSignUpView

app_name = 'user'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        success_url=reverse_lazy('user:password_reset_done')), name='password_reset'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('user:password_reset_complete')), name="password_reset_confirm"),
    path('', include('django.contrib.auth.urls',)),
    path('signup/', UserSignUpView.as_view(), name="signup"),
    path('profile/', ProfileUpdateView.as_view(), name="profile")
]
