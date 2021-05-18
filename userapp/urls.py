from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',  views.home, name="home"),
    path('register/', views.registration_view, name="register"),
    path('logout/',  views.logout_view, name="logout"),
    path('login/',  views.login_view, name="login"),
    path('profile/',  views.account_view, name="account"),


    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="userapp/password_reset.html"),
        name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="userapp/password_reset_done.html"),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="userapp/password_reset_complete.html"),
        name='password_reset_complete'),
]