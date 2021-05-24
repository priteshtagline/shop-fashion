from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^getCategoryByDepartment/$', views.get_category_by_department,
        name="get_category_by_department"),
    url(r'^getSubCategoryByCategory/$', views.get_subcategory_by_category,
        name="get_subcategory_by_category"),
    url(r'^getProductsByDepartment/$', views.get_products_by_department,
        name="get_products_by_department"),
    url(r'^getProductsByProduct/$', views.get_products_by_product,
        name="get_products_by_product"),

]
