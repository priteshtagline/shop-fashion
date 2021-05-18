from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='usersapp/home.html'), name='home'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.registration_view, name="register"),
]
