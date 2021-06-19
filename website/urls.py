from django.urls import path
from django.views.generic.base import TemplateView

from website.views.browse import BrowseListView
from website.views.home import HomeView
from website.views.product import ProductDeatilView
from website.views.search_product import SearchListView
from website.views.shoplook import ShopLookDetailView, ShopLookListView
from website.views.wishlist import WishlistView

app_name = 'website'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('privacy_policy', TemplateView.as_view(
        template_name='privacy_policy.html'), name='privacy_policy'),
    path('terms_conditions', TemplateView.as_view(
        template_name='terms_conditions.html'), name='terms_conditions'),
    path('product/<slug:slug>/<int:pk>',
         ProductDeatilView.as_view(), name='product'),
    path('browse/<department>/<category>/<subcategory>/',
         BrowseListView.as_view(), name='browse'),
    path('browse/<department>/<category>/',
         BrowseListView.as_view(), name='browse_category'),
    path('browse/<department>/',
         BrowseListView.as_view(), name='browse_department'),
    path('search/',
         SearchListView.as_view(), name='search_product'),
    path('shop-the-look/',
         ShopLookListView.as_view(), name='shoplook'),
    path('shop-the-look/<slug:slug>/<int:pk>',
         ShopLookDetailView.as_view(), name='shoplook_detail'),
    path('wishlist/',
         WishlistView.as_view(), name='wishlist'),
]
