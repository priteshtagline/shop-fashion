from django.urls import include, path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('product/<pk>', views.ProductDeatilView.as_view(), name='home'),
]
