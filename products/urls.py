from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^getCategoryByDepartment/$', views.get_category_by_department,
        name="get_category_by_department")
]
